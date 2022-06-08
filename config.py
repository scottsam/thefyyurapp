from os import environ,path,urandom
from dotenv import load_dotenv


# Grabs the folder where the script runs.
basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, '.env'))

# Enable debug mode.
DEBUG = True

# Connect to the database





class Config:
    FLASK_DEBUG = environ.get('DEBUG')
    FLASK_APP = environ.get('FLASK_APP')
    PGUSER = environ.get('PGUSER')
    SECRET_KEY = urandom(32)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

