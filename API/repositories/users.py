from models.user import User
from utils.database import db

def fetch_users():
    users = User.query.all()
    return users

def fetch_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user

def fetch_user_by_id(user_id):
    data = User.query.filter_by(id=user_id).first()
    return data

def create(data):
    data = User(data.get('email', None), data.get('password', None), data.get('username', None), data.get('role', None))
    db.session.add(data)
    db.session.commit()

def update(user_id, data):
    user = User.query.get_or_404(user_id)
    user.username = data.get('username', None)
    user.email = data.get('email', None)
    user.role = data.get('role', None)
    db.session.commit()

def delete(user_id):
    data = User.query.get_or_404(user_id)
    db.session.delete(data)
    db.session.commit()