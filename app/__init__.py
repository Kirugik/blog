from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
# from config import config_options 
from os import path 
from flask_login import LoginManager 


db = SQLAlchemy()
DB_NAME = "database.db"



def create_app(config_options):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "sksht52393nsy23"

    # tell flask the location of the database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # initializing the database with flask app
    db.init_app(app) 


    from .views import views 
    from .auth import auth 

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/") 


    from.models import User, Post, Comment, Like   

    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) 


    return app 


# creating the database
def create_database(app):
    # first, check if the database exists
    if not path.exists("app/" + DB_NAME):
        # if it does not exist, create one 
        db.create_all(app=app)
        print("Created database")