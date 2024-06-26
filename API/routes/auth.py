from flask import Blueprint, request
from utils.response import response_with
from utils import response as resp
from flask_jwt_extended import (
    create_access_token, create_refresh_token
)
import services.users as User

auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route("/login", methods=['POST'])
def login():
    data = request.json
    email = data.get('email', None)
    password = data.get('password', None)

    if email and password:
        user = User.authenticate(email, password)
        if user:
            role = user['role']
            email = user['email']
            username = user['username']
            sub = {
                "role": role,
                "email": email,
                "username": username
            }
            value = {
                'access_token': create_access_token(sub),
                'refresh_token': create_refresh_token(sub)
            }
            return response_with(resp.SUCCESS_200, value=value)

    return response_with(resp.SERVER_ERROR_404, message="Incorrect login credentials.")
