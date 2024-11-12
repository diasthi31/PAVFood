from src.model.Cozinha import Cozinha
from src.model.Base import db

def add_cozinha(id: int, nome: str) -> Cozinha:
    cozinha = Cozinha(id=id, nome=nome)
    db.session.add(cozinha)
    db.session.commit()
    return cozinha

def get_cozinhas() -> list[Cozinha]:
    cozinhas = db.session.query(Cozinha).all()
    return cozinhas

def get_cozinha(id: int) -> Cozinha:
    cozinha = db.session.query(Cozinha).get(id)
    return cozinha

def delete_cozinha(id: int):
    cozinha = db.session.query(Cozinha).get(id)
    db.session.delete(cozinha)
    db.session.commit()

def update_cozinha(nome: str) -> Cozinha:
    cozinha = db.session.query(Cozinha).get(id)
    cozinha.nome = nome
    db.session.commit()
    return cozinha