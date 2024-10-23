from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
bootstrap = Bootstrap(app)
login.login_view='index'
login.session_protection = 'strong'
from app import views, models