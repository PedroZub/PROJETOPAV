from .users_controller import UserItem, UserList
from .games_controller import GameItem, GameList
from .uhg_controller import UhgItem, UhgList

def initialize_endpoints(api):
    api.add_resource(UserItem, "/users/<int:user_id>")
    api.add_resource(UserList, "/users")
    api.add_resource(GameItem, "/games/<int:game_id>")
    api.add_resource(GameList, "/games")
    api.add_resource(UhgItem, "/Uhg/<int:uhg_id>")
    api.add_resource(UhgList, "/Uhg")

