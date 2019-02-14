from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    origin = Column(String(40))
    phase = Column(String(40))

    @property
    def serialize(self):
        """Return ingredient in serializeable format"""
        return {
            'name': self.name,
            'origin': self.origin,
            'id': self.id,
            'phase': self.phase,
        }


class Bowl(Base):
    __tablename__ = 'bowl'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(40))
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return bowl in serializeable format"""
        return {
            'name': self.name,
            'type': self.type,
            'id': self.id,
            'user_id': self.user_id,
        }


class Bowl_Ingredient(Base):
    __tablename__ = 'bowl_ingredient'

    id = Column(Integer, primary_key=True)
    bowl_id = Column(Integer, ForeignKey('bowl.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'))

    @property
    def serialize(self):
        """Return bowl's ingredient in easily serializeable format"""
        return {
            'bowl_id': self.bowl_id,
            'ingredient_id': self.ingredient_id,
            'id': self.id,
        }


engine = create_engine('sqlite:///bowls101.db')


Base.metadata.create_all(engine)