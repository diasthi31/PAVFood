from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base

class FormaDePagamento(Base):
    __tablename__ = "formaDePagamento"

    id = Column(
        "id",
        Integer,
        primary_key=True,
    )

    descricao = Column("descricao", String(250), nullable=False)