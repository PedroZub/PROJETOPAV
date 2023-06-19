from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, UniqueConstraint, Float, ForeignKey,Date
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()
db = SQLAlchemy()

engine = create_engine('mysql://root:root123@localhost:3306/new_schema')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(30), nullable=False)
    userhasgame = relationship("UserHasGame", back_populates="user")



class Game(Base):
    __tablename__ = 'games'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(30), nullable=False)
    platform = Column(String(20), nullable=False)
    duration = Column(Float)
    genre = Column(String(20), nullable=False)

    userhasgame = relationship("UserHasGame", back_populates="game")


class UserHasGame(Base):
    __tablename__ = 'user_has_game'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))
    rate = Column(Integer)
    review = Column(String(255))
    user = relationship("User", back_populates="userhasgame")
    game = relationship("Game", back_populates="userhasgame")


if __name__ == "__main__":
    Base.metadata.create_all(engine)