import datetime
from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.auth.model import User
from errors import (EmailAlreadyExistsError,
                    SchemaValidationError,
                    InternalServerError,
                    UnauthorizedError)


class SignUpApi(Resource):
    @staticmethod
    def post():
        try:
            body = request.get_json()
            user = User(**body)
            user.generate_password()
            user.save()
            user_id = user.id
            return {"id": str(user_id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception:
            raise InternalServerError


class LoginApi(Resource):
    @staticmethod
    def post():
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id),
                                               expires_delta=expires)
            return {'token': access_token}, 200
        except (DoesNotExist, UnauthorizedError):
            raise UnauthorizedError
        except Exception:
            raise InternalServerError
