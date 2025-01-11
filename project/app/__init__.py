from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os

from app.extensions import db
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bds.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'BDS2425'  # clé secrète

  

    # Initialiser les extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Enregistrer les blueprints
    from .views import admin_bp, user_bp
    app.register_blueprint(user_bp, url_prefix='/')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app

