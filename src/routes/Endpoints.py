from src.controller.CozinhaController import CozinhaItem, CozinhaList
from src.controller.RestauranteController import RestauranteItem, RestauranteList

def initialize_endpoints(api):
    api.add_resource(CozinhaItem, "/cozinhas/<int:cozinhaId>")
    api.add_resource(CozinhaList, "/cozinhas")
    
    api.add_resource(RestauranteItem, "/restaurantes/<int:restauranteId>")
    api.add_resource(RestauranteList, "/restaurantes")