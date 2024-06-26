from flask import Flask, request
import logging
from utils.database import db
from routes.auth import auth_blueprint
from routes.users import users_blueprint
from routes.reviews import reviews_blueprint
from models.review import Review
from utils.response import response_with
from utils import response as resp
from flask_jwt_extended import (
    JWTManager, decode_token, current_user
)
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SALT'] = os.getenv('SALT')

    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    database = os.getenv('DB_DATABASE')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@{host}/{database}'
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    
    db.init_app(app)
    jwt = JWTManager(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(reviews_blueprint)

    @jwt.user_lookup_loader
    def user_lookup_loader(_jwt_header, jwt_data):
        identity = jwt_data['sub']
        email = identity['email']
        role = identity['role']
        username =  identity['username']
        return {
            'email': email,
            'role': role,
            'username': username
        }

    @app.before_request
    def check_indentity():
        if "Authorization" in request.headers:
            token = None
            result = None
            token = request.headers["Authorization"].split(" ")[1]
            result = decode_token(token).get('sub')
            if isinstance(result, dict):
                if not('email' in result and 'username' in result and 'role' in result):
                    return response_with(resp.UNAUTHORIZED_403)
            else:
                return response_with(resp.UNAUTHORIZED_403)
            
    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)
    
    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.NOT_FOUND_HANDLER_404)

    with app.app_context():
       # Initialize DB
       db.create_all()

    #    Seeding
    #    db.session.add(Review('Description', 'admin@example.com', '5'))
    #    db.session.add(Review('Desc', 'guest@example.com', '5'))
    #    db.session.commit()

    return app

app = create_app()


if __name__ == "__main__":
  app.run(host="127.0.0.1", use_reloader=True, port='8000')