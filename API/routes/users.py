from flask import Blueprint, request
import services.users as User
from utils.response import response_with
from utils import response as resp
from flask_jwt_extended import (
    jwt_required
)
from utils.middleware import admin_access

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route('/users', methods=['GET'])
@jwt_required()
@admin_access
def index():
    datas = User.fetch_all()
    return response_with(resp.SUCCESS_200, value={"datas": datas})

@users_blueprint.route('/users', methods=['POST'])
def create():
    data = request.json
    isSucess = User.create(data)
    if isSucess:
        return response_with(resp.CREATED_201, message="New User has been recorded")
    return response_with(resp.SERVER_ERROR_500, message="Something wrong with your code")

@users_blueprint.route('/users/<user_id>', methods=['GET'])
@jwt_required()
@admin_access
def read(user_id):
    data = User.fetch_by_id(user_id)
    return response_with(resp.SUCCESS_200, value={"data": data})

@users_blueprint.route('/users/<user_id>', methods=['PUT'])
@jwt_required()
@admin_access
def update(user_id):
    data = request.json
    isSucess = User.update(user_id, data)
    if isSucess:
        return response_with(resp.SUCCESS_200, message="User has been successfuly updated")
    return response_with(resp.SERVER_ERROR_500, message="Something wrong with your code")

@users_blueprint.route('/users/<user_id>', methods=['DELETE'])
@jwt_required()
@admin_access
def delete(user_id):
    isSucess = User.delete(user_id)
    if isSucess:
        return response_with(resp.SUCCESS_200, message="User has been successfuly deleted")
    return response_with(resp.SERVER_ERROR_500, message="Something wrong with your code")