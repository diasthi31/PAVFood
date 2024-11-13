from src.controller.CozinhaController import CozinhaItem, CozinhaList
from src.controller.RestauranteController import RestauranteItem, RestauranteList

def initialize_endpoints(api):
    api.add_resource(CozinhaItem, "/api/cozinhas/<int:cozinhaId>")
    api.add_resource(CozinhaList, "/api/cozinhas")
    
    api.add_resource(RestauranteItem, "/api/restaurantes/<int:restauranteId>")
    api.add_resource(RestauranteList, "/api/restaurantes")