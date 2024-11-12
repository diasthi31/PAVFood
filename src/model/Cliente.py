from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(
        "id",
        Integer,
        primary_key=True,
    )
    
    nome = Column("nome", String(250), nullable=False)
    cpf = column("cpf", String(250), nullable=False)
    email = Column("salario", String(250), nullable=False)
    telefone = Column("telefone", String(250), nullable=True)
    ativo = Column("ativo", Boolean, nullable=False)

    pedidos = relationship("Pedido", back_populates="cliente")