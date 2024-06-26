from utils.database import db
import enum
from uuid import uuid4

class Role(enum.Enum):
    def __str__(self):
        return str(self.value)
    
    User = "User"
    Admin = "Admin"

class User(db.Model):
    id = db.Column(db.String(100), primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(1000))
    role = db.Column(db.Enum(Role))

    def __repr__(self):
        return f'<User {self.id}>'
    
    def __init__(self, email, password, username, role):
        self.id = str(uuid4())
        self.email = email
        self.password = password
        self.username = username
        self.role = role

    def obj_to_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}