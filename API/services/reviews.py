from repositories import reviews as review_repositories

def fetch_all():
    datas = review_repositories.fetch_reviews()
    datas = [data.obj_to_dict() for data in datas]
    return datas

def fetch_by_id(review_id):
    data = review_repositories.fetch_review_by_id(review_id)
    data = data.obj_to_dict()
    return data

def create(data):
    try:
        review_repositories.create(data)
        return True
    except:
        return False

def update(review_id, data):
    try:
        review_repositories.update(review_id, data)
        return True
    except:
        return False

def delete(review_id):
    try:
        review_repositories.delete(review_id)
        return True
    except:
        return False