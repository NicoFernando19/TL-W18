from repositories import users as user_repositories
from flask import current_app as app
import hashlib

def authenticate(email, provided_password):
    user = user_repositories.fetch_user_by_email(email)
    user = user.obj_to_dict()
    if user:
        is_password_match = check_password(provided_password, user['password'])
        if is_password_match:
            return user
    return None

def check_password(provided_password, saved_password_hash):
    password_hash = hash_password(provided_password)
    return password_hash == saved_password_hash

def hash_password(password):
    salt = app.config.get('SALT')
    str_to_hash = password.encode('utf-8') + salt.encode('utf-8')
    password_hash = hashlib.sha512(str_to_hash).hexdigest()
    return password_hash

def fetch_all():
    datas = user_repositories.fetch_users()
    datas = [data.obj_to_dict() for data in datas]
    return datas

def fetch_by_email(email):
    data = user_repositories.fetch_user_by_email(email)
    data = data.obj_to_dict()
    return data

def fetch_by_id(user_id):
    data = user_repositories.fetch_user_by_id(user_id)
    data = data.obj_to_dict()
    return data

def create(data):
    try:
        password = hash_password(data.get('password'))
        data['password'] = password
        user_repositories.create(data)
        return True
    except:
        return False

def update(user_id, data):
    try:
        user_repositories.update(user_id, data)
        return True
    except:
        return False

def delete(user_id):
    try:
        user_repositories.delete(user_id)
        return True
    except:
        return False