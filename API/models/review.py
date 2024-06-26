from utils.database import db
from uuid import uuid4

class Review(db.Model):
    id = db.Column(db.String(100), primary_key=True) 
    email = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    rating = db.Column(db.String(100))

    def __repr__(self):
        return f'<Review {self.id}>'

    def __init__(self, description, email, rating):
        self.id = str(uuid4())
        self.description = description
        self.email = email
        self.rating = rating

    def obj_to_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}