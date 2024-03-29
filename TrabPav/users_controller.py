from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from .users_repository import get_user, get_users, add_user, update_user, delete_user, select_user

response_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "age": fields.Integer,
    "gender": fields.String,
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("name", type=str, help="", required=True)
request_parser.add_argument("age", type=int, help="", required=True)
request_parser.add_argument("gender", type=str, help="", required=True)


class UserItem(Resource):
    @marshal_with(response_fields)
    def get(self, user_id):
        try:
            user = get_user(user_id)
            if not user:
                abort(404, message="Resource not found")
            return user, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, user_id):
        try:
            delete_user(user_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def put(self, user_id):
        try:
            args = request_parser.parse_args(strict=True)
            user = update_user(**args, id=user_id)
            return user, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class UserList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            if request.args:
                select_user(request.args['name'])
            else:
                return get_users(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            user = add_user(**args)
            return user, 201
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")