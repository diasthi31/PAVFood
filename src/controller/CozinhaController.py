from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.service.CozinhaService import deleteCozinha, updateCozinha, addCozinha, getCozinha, getCozinhas

class CozinhaResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()

class CozinhaRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()

    @validates("nome")
    def validate_name(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_\s]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )
        
class CozinhaItem(MethodResource, Resource):
    @marshal_with(CozinhaResponseSchema)
    def get(self, cozinhaId):
        try:
            cozinha = getCozinha(cozinhaId)
            if not cozinha:
                abort(404, message="Resource not found")
            return cozinha, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, cozinhaId):
        try:
            deleteCozinha(cozinhaId)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(CozinhaRequestSchema, location=("form"))
    @marshal_with(CozinhaResponseSchema)
    def put(self, cozinhaId, **kwargs):
        try:
            cozinha = updateCozinha(**kwargs, id=cozinhaId)
            return cozinha, 200
        except (OperationalError, IntegrityError):
           abort(500, message="Internal Server Error")


class CozinhaList(MethodResource, Resource):
    @marshal_with(CozinhaResponseSchema(many=True))
    def get(self):
        try:
            return getCozinhas(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(CozinhaRequestSchema, location=("form"))
    @marshal_with(CozinhaResponseSchema)
    def post(self, **kwargs):
        try:
            cozinha = addCozinha(**kwargs)
            return cozinha, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))