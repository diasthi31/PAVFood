from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.RestauranteService import updateRestaurante, getRestaurantes, deleteRestaurante, addRestaurante, getRestaurante

class RestauranteResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    cnpj = fields.Str()
    taxaFrete = fields.Float()
    cozinha_id = fields.Int()
    produto_id = fields.Int()

class RestauranteRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    cnpj = fields.Float()
    taxaFrete = fields.Float()
    cozinha_id = fields.Int()
    produto_id = fields.Int()
        
class RestauranteItem(MethodResource, Resource):
    @marshal_with(RestauranteResponseSchema)
    def get(self, restauranteId):
        try:
            restaurante = getRestaurante(restauranteId)
            if not restaurante:
                abort(404, message="Resource not found")
            return restaurante, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, restauranteId):
        try:
            deleteRestaurante(restauranteId)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(RestauranteRequestSchema, location=("form"))
    @marshal_with(RestauranteResponseSchema)
    def put(self, restauranteId, **kwargs):
        try:
            restaurante = updateRestaurante(**kwargs, id=restauranteId)
            return restaurante, 200
        except (OperationalError, IntegrityError):
           abort(500, message="Internal Server Error")


class RestauranteList(MethodResource, Resource):
    @marshal_with(RestauranteResponseSchema(many=True))
    def get(self):
        try:
            return getRestaurantes(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(RestauranteRequestSchema, location=("form"))
    @marshal_with(RestauranteResponseSchema)
    def post(self, **kwargs):
        try:
            restaurante = addRestaurante(**kwargs)
            return restaurante, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))