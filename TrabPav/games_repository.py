import sqlalchemy
from .models import Game, db

def get_games() -> sqlalchemy.orm.query.Query:
    """
    Get all games stored in the database.

    Returns:
        games (Game) -- contains all games registered.
    """
    Games = db.session.query(Game).all()
    return Games


def get_game(id: int) -> Game:
    """
    Get a game stored in the database according to the id.

    Arguments:
        id (int) -- object id.

    Returns:
        game (Game) -- registered game infomation.
    """
    game = db.session.query(Game).get(id)
    return game


def delete_game(id: int):
    """
    Delete a game stored in the database according to the id.

    Arguments:
        id (int) -- object id.
    """
    game = db.session.query(Game).get(id)
    db.session.delete(game)
    db.session.commit()


def select_game(name: str) -> sqlalchemy.orm.query.Query:
    """
    Get a game stored in the database according to the id.

    Arguments:
        id (int) -- object id.

    Returns:
        game (Game) -- registered game infomation.
    """
    print(name)
    game = db.session.query(Game).filter_by(name=name).all()
    return game


def add_game(name: str, duration: float,platform: str, genre: str) -> Game:
    """
    Insert a game in the database.
    """
    game = Game(name=name, duration=duration,platform=platform, genre=genre)
    db.session.add(game)

    db.session.commit()

    return game

def update_game(name: str, duration: float,platform: str, genre: str, id: int) -> Game:
    """
    Insert a game in the database.
    """
    game = db.session.query(Game).get(id)
    
    game.name = name
    game.duration = duration
    game.platform = platform
    game.genre = genre

    db.session.commit()

    return game