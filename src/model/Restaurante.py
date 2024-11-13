from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .Base import db

class Restaurante(db.Model):
    __tablename__ = "restaurante"

    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(250), nullable=False)
    cnpj = Column("cnpj", String(250), nullable=False)
    taxaFrete = Column("taxaFrete", Float, nullable=False)

    cozinha_id = Column(Integer, ForeignKey("cozinha.id", ondelete="SET NULL"), nullable=True)
    cozinha = relationship("Cozinha", back_populates="restaurantes")

    produtos = relationship("Produto", back_populates="restaurante", lazy="dynamic")

from .Produto import Produto