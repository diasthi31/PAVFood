from src.model.Restaurante import Restaurante
from src.repository.RestauranteRepository import update_restaurante, delete_restaurante, get_restaurante, add_restaurante, get_restaurantes

def addRestaurante(id: int, nome: str, cnpj: str, taxaFrete: float, cozinha_id=None, produto_id=None) -> Restaurante:
    if(id is None or id == '' or nome is None or nome == '' or cnpj is None or cnpj == '' or cozinha_id is None or cozinha_id == '' or produto_id is None or produto_id == ''):
        raise Exception
    if(taxaFrete < 0):
        raise Exception
    
    return add_restaurante(id, nome, cnpj, taxaFrete, cozinha_id, produto_id)

def getRestaurantes() -> list[Restaurante]:
    return get_restaurantes()

def getRestaurante(id: int) -> Restaurante:
    return get_restaurante(id)

def deleteRestaurante(id: int):
    delete_restaurante(id)

def updateRestaurante(id: int, nome: str, cnpj:str, taxaFrete: float, cozinha_id: int, produto_id: int):
    return update_restaurante(id=id, nome=nome, cnpj=cnpj, taxaFrete=taxaFrete, cozinha_id=cozinha_id, produto_id=produto_id)