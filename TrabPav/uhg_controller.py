from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from .uhg_repository import get_uhgs, get_uhg, add_uhg, update_uhg, delete_uhg, select_uhg


response_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "game_id": fields.Integer,
    "rate": fields.Integer,
    "review": fields.String
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("user_id", type=int, help="", required=True)
request_parser.add_argument("game_id", type=int, help="", required=True)
request_parser.add_argument("rate", type=int, help="", required=True)
request_parser.add_argument("review", type=str, help="", required=True)


class UhgItem(Resource):
    @marshal_with(response_fields)
    def get(self, uhg_id):
        try:
            uhg = get_uhg(uhg_id)
            if not uhg:
                abort(404, message="Resource not found")
            return uhg, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, uhg_id):
        try:
            delete_uhg(uhg_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def put(self, uhg_id):
        try:
            args = request_parser.parse_args(strict=True)
            uhg = update_uhg(**args, id=uhg_id)
            return uhg, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class UhgList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            if request.args:
                select_uhg(request.args['name'])
            else:
                return get_uhgs(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            uhg = add_uhg(**args)
            return uhg, 201
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")