from models.user import User
from models.account import Account

def fetch_users():
    users = User.query.all()
    return users

def fetch_user(user_id):
    user = User.query.join(Account, User.id == Account.user_id).add_columns(User.id, User.email, User.username, Account.account_number, Account.account_type).filter_by(id=int(user_id)).first()
    return user

def fetch_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user

