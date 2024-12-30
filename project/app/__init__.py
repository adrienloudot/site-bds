from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bds.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  

    # Initialiser les extensions
    db.init_app(app)

    # Enregistrer les blueprints
    from .views import admin_bp, user_bp
    app.register_blueprint(user_bp, url_prefix='/')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app

