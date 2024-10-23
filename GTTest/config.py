import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'qhufdewnfd'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'bags.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

