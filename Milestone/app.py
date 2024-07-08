from flask import Flask
from utils.database import db
from routes.users import users_routes
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv
import os 
from datetime import timedelta

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
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=7)

    db.init_app(app)
    jwt = JWTManager(app)

    app.register_blueprint(users_routes)

    with app.app_context():
        db.create_all()
    

    return app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)