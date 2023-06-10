import sqlalchemy
from .models import UserHasGame, db

#uhg = userhasgame
def get_uhgs() -> sqlalchemy.orm.query.Query:
    """
    Get all uhgs stored in the database.

    Returns:
        uhg (UserHasGame) -- contains all games registered.
    """
    uhg = db.session.query(UserHasGame).all()
    return uhg


def get_uhg(id: int) -> UserHasGame:
    """
    Get a uhg stored in the database according to the id.

    Arguments:
        id (int) -- object id.

    Returns:
        uhg (UserHasGame) -- registered uhg infomation.
    """
    uhg = db.session.query(UserHasGame).get(id)
    return uhg


def delete_uhg(id: int):
    """
    Delete a uhg stored in the database according to the id.

    Arguments:
        id (int) -- object id.
    """
    uhg = db.session.query(UserHasGame).get(id)
    db.session.delete(uhg)
    db.session.commit()


def select_uhg(name: str) -> sqlalchemy.orm.query.Query:
    """
    Get a uhg stored in the database according to the id.

    Arguments:
        id (int) -- object id.

    Returns:
        uhg (UserHasGame) -- registered uhg infomation.
    """
    print(name)
    uhg = db.session.query(UserHasGame).filter_by(name=name).all()
    return uhg


def add_uhg(user_id:int, game_id:int,rate: int, review: str) -> UserHasGame:
    """
    Insert a uhg in the database.
    """
    uhg = UserHasGame(user_id=user_id, game_id=game_id,rate=rate, review=review)
    db.session.add(uhg)

    db.session.commit()

    return uhg

def update_uhg(user_id:int, game_id:int,rate: int, review: str, id: int) -> UserHasGame:
    """
    Insert a uhg in the database.
    """
    uhg = db.session.query(UserHasGame).get(id)
    
    uhg.user_id = user_id
    uhg.game_id = game_id
    uhg.rate = rate
    uhg.review = review

    db.session.commit()

    return uhg