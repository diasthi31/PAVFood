from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .Base import Base

class Pedido(Base):
    __tablename__ = "pedido"

    id = Column(
        "id",
        Integer,
        primary_key=True,
    )
    
    codigo = Column("codigo", String(250), nullable=False)
    subTotal = Column("subTotal", Float, nullable=False)
    taxaFrete = Column("taxaFrete", Float, nullable=False)
    dataCriacao = Column("dataCriacao", String, nullable=False)
    statusPedido = Column("statusPedido", String(250), nullable=False)

    itemPedido_fk = ForeignKey("itemPedido.id", ondelete="SET NULL")
    itemPedido_id = Column("itemPedido_id", itemPedido_fk, nullable=False)
    itemPedido = relationship('ItemPedido', back_populates='pedido', uselist=True)

    restaurante_fk = ForeignKey("restaurante.id", ondelete="SET NULL")
    restaurante_id = Column("restaurante_id", restaurante_fk, nullable=False)
    restaurante = relationship("Restaurante", back_populates="pedido")

    cliente_fk = ForeignKey("cliente.id", ondelete="SET NULL")
    cliente_id = Column("cliente_id", cliente_fk, nullable=False)
    cliente = relationship("Cliente", back_populates="pedido")

    formaDePagamento_fk = ForeignKey("formaDePagamento.id", ondelete="SET NULL")
    formaDePagamento_id = Column("formaDePagamento_id", formaDePagamento_fk, nullable=False)
    formaDePagamento = relationship("FormaDePagamento", back_populates="pedido")