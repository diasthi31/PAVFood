from flask import Flask
from flask_restful import Api
from src.routes.Endpoints import initialize_endpoints
from src.controller.CozinhaController import CozinhaItem, CozinhaList
from src.controller.RestauranteController import RestauranteItem, RestauranteList
from flask_apispec import FlaskApiSpec

app = Flask(__name__)

app.config.update({
    'APISPEC_SWAGGER_URL': '/swagger/',  
    'APISPEC_SPEC_URL': '/swagger.json'  
})

api = Api(app)a
initialize_endpoints(api)

docs = FlaskApiSpec(app)
docs.register(CozinhaItem)
docs.register(CozinhaList)
docs.register(RestauranteItem)
docs.register(RestauranteList)

@app.route('/swagger/')
def swagger_ui():
    return app.send_static_file('swagger-ui/index.html')

if __name__ == '__main__':
    app.run(debug=True)
