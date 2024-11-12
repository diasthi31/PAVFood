from src.model.Cozinha import Cozinha
from src.repository.CozinhaRepository import update_cozinha, delete_cozinha, get_cozinha, add_cozinha, get_cozinhas

def addCozinha(id: int, nome: str) -> Cozinha:
    if(id is None or id == '' or nome is None or nome == ''):
        raise Exception
    
    return add_cozinha(id, nome)

def getCozinhas() -> list[Cozinha]:
    return get_cozinhas()

def getCozinha(id: int) -> Cozinha:
    return get_cozinha(id)

def deleteCozinha(id: int):
    delete_cozinha(id)

def updateCozinha(id: int, nome: str):
    return update_cozinha(id=id, nome=nome)