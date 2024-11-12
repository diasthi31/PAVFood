from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from .Base import db

class Produto(db.Model):
    __tablename__ = "produto"

    id = Column(
        "id",
        Integer,
        primary_key=True,
    )

    nome = Column("nome", String(250), nullable=False)
    descricao = Column("descricao", String(250), nullable=False)
    preco = Column("preco", Float, nullable=False)
    ativo = Column("ativo", Boolean, nullable=True)

    restaurante = relationship('Restaurante', back_populates='produtos')