from models.review import Review
from utils.database import db

def fetch_reviews():
    datas = Review.query.all()
    return datas

def fetch_review_by_id(review_id):
    data = Review.query.filter_by(id=review_id).first()
    return data

def create(data):
    data = Review(data.get('description', None), data.get('email', None), data.get('rating', None))
    db.session.add(data)
    db.session.commit()

def update(review_id, data):
    review = Review.query.get_or_404(review_id)
    review.email = data.get('email', None)
    review.rating = data.get('rating', None)
    review.description = data.get('description', None)
    db.session.commit()

def delete(review_id):
    data = Review.query.get_or_404(review_id)
    db.session.delete(data)
    db.session.commit()
