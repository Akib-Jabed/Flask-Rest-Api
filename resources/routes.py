from flask_restful import Api
from resources.movie.resource import MoviesApi, MovieApi
from resources.auth.resource import SignUpApi, LoginApi

# from resources.reset_password import ResetPassword, ForgetPassword

api = Api()

# def initialize_routes(api):
api.add_resource(MoviesApi, '/api/movies')
api.add_resource(MovieApi, '/api/movies/<movie_id>')

api.add_resource(SignUpApi, '/api/auth/signup')
api.add_resource(LoginApi, '/api/auth/login')

# api.add_resource(ForgetPassword, '/api/auth/forgot')
# api.add_resource(ResetPassword, '/api/auth/reset')
