import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '') or \
        'sqlite:///' + os.path.join(basedir, 'gro.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
