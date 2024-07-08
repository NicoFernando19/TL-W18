from flask import Blueprint, request, jsonify
from services import user as user_service

users_routes = Blueprint('users_routes', __name__)

@users_routes.route('/users', methods=['GET'])
def fetch_users():
    users = user_service.fetch_user_by_id()
    return jsonify({ "users": users})