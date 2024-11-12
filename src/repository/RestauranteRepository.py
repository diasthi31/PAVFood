from src.model.Restaurante import Restaurante
from src.model.Base import db

def add_restaurante(id: int, nome: str, cnpj:str, taxaFrete: float, cozinha_id=None, produto_id=None) -> Restaurante:
    restaurante = Restaurante(id=id, nome=nome, cnpj=cnpj, taxaFrete=taxaFrete, cozinha_id=cozinha_id, produto_id=produto_id)
    db.session.add(restaurante)
    db.session.commit()
    return restaurante

def get_restaurantes() -> list[Restaurante]:
    restaurantes = db.session.query(Restaurante).all()
    return restaurantes

def get_restaurante(id: int) -> Restaurante:
    restaurante = db.session.query(Restaurante).get(id)
    return restaurante

def delete_restaurante(id: int):
    restaurante = db.session.query(Restaurante).get(id)
    db.session.delete(restaurante)
    db.session.commit()

def update_restaurante(id: int, nome: str, cnpj:str, taxaFrete: float, cozinha_id=None, produto_id=None) -> Restaurante:
    restaurante = db.session.query(Restaurante).get(id)
    restaurante.nome = nome
    restaurante.cnpj = cnpj
    restaurante.taxaFrete = taxaFrete
    restaurante.cozinha_id = cozinha_id
    restaurante.produto_id = produto_id
    db.session.commit()
    return restaurante