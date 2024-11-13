from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .Base import db

class Produto(db.Model):
    __tablename__ = "produto"

    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String(250), nullable=False)
    descricao = Column("descricao", String(250), nullable=False)
    preco = Column("preco", Float, nullable=False)
    ativo = Column("ativo", Boolean, nullable=True)

    restaurante_id = Column(Integer, ForeignKey("restaurante.id"), nullable=False)
    restaurante = relationship("Restaurante", back_populates="produtos")
