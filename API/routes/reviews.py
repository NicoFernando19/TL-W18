from flask import Blueprint, request
import services.reviews as Review
from utils.response import response_with
from utils import response as resp
from flask_jwt_extended import ( 
    jwt_required
)

reviews_blueprint = Blueprint('reviews_blueprint', __name__)

@reviews_blueprint.route('/reviews', methods=['GET'])
def index():
    datas = Review.fetch_all()
    return response_with(resp.SUCCESS_200, value={"datas": datas})

@reviews_blueprint.route('/reviews', methods=['POST'])
@jwt_required()
def create():
    data = request.json
    isSucess = Review.create(data)
    if isSucess:
        return response_with(resp.CREATED_201, message="Your Review has been recorded")
    return response_with(resp.SERVER_ERROR_500, message="Something wrong with your code")

@reviews_blueprint.route('/reviews/<review_id>', methods=['GET'])
@jwt_required()
def read(review_id):
    data = Review.fetch_by_id(review_id)
    return response_with(resp.SUCCESS_200, value={"data": data})

@reviews_blueprint.route('/reviews/<review_id>', methods=['PUT'])
@jwt_required()
def update(review_id):
    data = request.json
    isSucess = Review.update(review_id, data)
    if isSucess:
        return response_with(resp.SUCCESS_200, message="Your Review has been successfuly updated")
    return response_with(resp.SERVER_ERROR_500, message="Something wrong with your code")

@reviews_blueprint.route('/reviews/<review_id>', methods=['DELETE'])
@jwt_required()
def delete(review_id):
    isSucess = Review.delete(review_id)
    if isSucess:
        return response_with(resp.SUCCESS_200, message="Your Review has been successfuly deleted")
    return response_with(resp.SERVER_ERROR_500, message="Something wrong with your code")