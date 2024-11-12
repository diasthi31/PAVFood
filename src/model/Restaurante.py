from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .Base import db

class Restaurante(db.Model):
    __tablename__ = "restaurante"

    id = Column(
        "id",
        Integer,
        primary_key=True,
    )

    nome = Column("nome", String(250), nullable=False)
    cnpj = Column("cnpj", String(250), nullable=False)
    taxaFrete = Column("taxaFrete", Float, nullable=False)
    
    cozinha_fk = ForeignKey("cozinha.id", ondelete="SET NULL")
    cozinha_id = Column("cozinha_id", cozinha_fk, nullable=False)
    #produto_fk = ForeignKey("produto.id", ondelete="SET NULL")
    #produto_id = Column("produto_id", produto_fk, nullable=False)

    cozinha = relationship('Cozinha', back_populates='restaurantes')
    #produtos = relationship('Produto', backref='restaurante', uselist=True)
    # pedidos = relationship("Pedido", back_populates="restaurante")