from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine import (FieldDoesNotExist,
                         NotUniqueError,
                         DoesNotExist,
                         ValidationError,
                         InvalidQueryError)
from resources.movie.model import Movie
from resources.auth.model import User
from errors import (SchemaValidationError,
                    MovieAlreadyExistsError,
                    InternalServerError,
                    UpdatingMovieError,
                    DeletingMovieError,
                    MovieNotExistsError)


# movies = Blueprint('movies', __name__)


class MoviesApi(Resource):
    @staticmethod
    @jwt_required
    def get():
        try:
            _movies = Movie.objects().to_json()
            return Response(_movies, mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

    @staticmethod
    @jwt_required
    def post():
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            movie = Movie(**body, added_by=user)
            movie.save()
            insert_id = movie.id
            return {'id': str(insert_id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise MovieAlreadyExistsError
        except Exception:
            raise InternalServerError


class MovieApi(Resource):
    @staticmethod
    @jwt_required
    def get(movie_id):
        try:
            movie = Movie.objects.get(id=movie_id).to_json()
            return Response(movie, mimetype="application/json", status=200)
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception:
            raise InternalServerError

    @staticmethod
    @jwt_required
    def put(movie_id):
        try:
            user_id = get_jwt_identity()
            movie = Movie.objects.get(id=movie_id, added_by=user_id)
            body = request.get_json()
            movie.update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingMovieError
        except Exception:
            raise InternalServerError

    @staticmethod
    @jwt_required
    def delete(movie_id):
        try:
            user_id = get_jwt_identity()
            movie = Movie.objects.get(id=movie_id, added_by=user_id)
            movie.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingMovieError
        except Exception:
            raise InternalServerError

# @movies.route('/movies')
# def get_movies():
#     _movies = Movie.objects().to_json()
#     return Response(_movies, mimetype="application/json", status=200)
#
#
# @movies.route('/movies', methods=['POST'])
# def add_movie():
#     body = request.get_json()
#     movie = Movie(**body).save()
#     insert_id = movie.id
#     return {'id': str(insert_id)}, 200
#
#
# @movies.route('/movie/<movie_id>')
# def get_movie(movie_id):
#     movie = Movie.objects.get(id=movie_id).to_json()
#     return Response(movie, mimetype="application/json", status=200)
#
#
# @movies.route('/movie/<movie_id>', methods=['PUT'])
# def update_movie(movie_id):
#     body = request.get_json()
#     Movie.objects.get(id=movie_id).update(**body)
#     return '', 200
#
#
# @movies.route('/movie/<movie_id>', methods=['DELETE'])
# def delete_movie(movie_id):
#     Movie.objects.get(id=movie_id).delete()
#     return '', 200
