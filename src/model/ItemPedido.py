from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .Base import Base

class ItemPedido(Base):
    __tablename__ = "itemPedido"

    id = Column(
        "id",
        Integer,
        primary_key=True,
    )

    quantidade = Column("quantidade", Integer, nullable=False)
    precoUnitario = Column("precoUnitario", Float, nullable=False)
    precoTotal = Column("precoTotal", Float, nullable=False)
    observacao = Column("observacao", String(250), nullable=True)

    item = relationship('Item', back_populates='itemPedido')