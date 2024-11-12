from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .Base import db

class Cozinha(db.Model):
    __tablename__ = "cozinha"

    id = Column(
        "id",
        Integer,
        primary_key=True,
    )

    nome = Column("nome", String(250), nullable=False)

    restaurantes = relationship('Restaurante', back_populates='cozinha', uselist=True)