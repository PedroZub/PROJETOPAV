import sqlalchemy
from .models import User, db

def get_users() -> sqlalchemy.orm.query.Query:
    """
    Get all users stored in the database.

    Returns:
        users (User) -- contains all users registered.
    """
    users = db.session.query(User).all()
    return users


def get_user(id: int) -> User:
    """
    Get a user stored in the database according to the id.

    Arguments:
        id (int) -- object id.

    Returns:
        user (User) -- registered user infomation.
    """
    user = db.session.query(User).get(id)
    return user


def delete_user(id: int):
    """
    Delete a user stored in the database according to the id.

    Arguments:
        id (int) -- object id.
    """
    user = db.session.query(User).get(id)
    db.session.delete(user)
    db.session.commit()


def select_user(name: str) -> sqlalchemy.orm.query.Query:
    """
    Get a user stored in the database according to the id.

    Arguments:
        id (int) -- object id.

    Returns:
        user (User) -- registered user infomation.
    """
    print(name)
    user = db.session.query(User).filter_by(name=name).all()
    return user


def add_user(name: str, age: int, gender: str) -> User:
    """
    Insert a user in the database.
    """
    user = User(name=name, age=age, gender=gender)
    db.session.add(user)

    db.session.commit()

    return user

def update_user(name: str, age: int, gender: str, id: int) -> User:
    """
    Insert a user in the database.
    """
    user = db.session.query(User).get(id)
    
    user.name = name
    user.age = age
    user.gender = gender

    db.session.commit()

    return user