from flask import Flask
from utils.database import db
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv
import os 

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    username = os.getenv('DB_USERNAME')
    database = os.getenv('DB_DATABASE')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    database_uri = f"mysql://{username}:{password}@{host}/{database}"
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    db.init_app(app)
    

    return app