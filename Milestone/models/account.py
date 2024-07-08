from utils.database import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    account_type = db.Column(db.String(255))
    account_number = db.Column(db.String(255), unique=True)
    # user = db.relationship('User', foreign_keys=[user_id])
    
    