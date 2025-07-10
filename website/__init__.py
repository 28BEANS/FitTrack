from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = "database.db"
DB_PATH = os.path.join("instance", DB_NAME)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "safljnefiefoqno"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    return app

def create_database(app):
    if not os.path.exists(DB_PATH):
        with app.app_context(): 
            db.create_all()
        print("Created Database!")
