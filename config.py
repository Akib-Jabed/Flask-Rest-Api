import ast
import os
from dotenv import load_dotenv

base_directory = os.path.dirname(__file__)
load_dotenv(os.path.join(base_directory, '.env'))


class ConfigClass(object):
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    MONGODB_SETTINGS = ast.literal_eval(os.environ.get('MONGODB_SETTINGS'))
