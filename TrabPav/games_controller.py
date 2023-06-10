from flask_restful import Resource, abort, fields, marshal_with, reqparse, request
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from .games_repository import get_game, get_games, add_game, update_game, delete_game, select_game

response_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "duration": fields.Float,
    "platform": fields.String,
    "genre": fields.String
}

request_parser = reqparse.RequestParser(bundle_errors=True)
request_parser.add_argument("name", type=str, help="", required=True)
request_parser.add_argument("duration", type=float, help="", required=True)
request_parser.add_argument("platform", type=str, help="", required=True)
request_parser.add_argument("genre", type=str, help="", required=True)


class GameItem(Resource):
    @marshal_with(response_fields)
    def get(self, game_id):
        try:
            game = get_game(game_id)
            if not game:
                abort(404, message="Resource not found")
            return game, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, game_id):
        try:
            delete_game(game_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def put(self, game_id):
        try:
            args = request_parser.parse_args(strict=True)
            game = update_game(**args, id=game_id)
            return game, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class GameList(Resource):
    @marshal_with(response_fields)
    def get(self):
        try:
            if request.args:
                select_game(request.args['name'])
            else:
                return get_games(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @marshal_with(response_fields)
    def post(self):
        try:
            args = request_parser.parse_args(strict=True)
            game = add_game(**args)
            return game, 201
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")