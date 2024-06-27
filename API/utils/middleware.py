from functools import wraps
from models.user import Role
from utils.response import response_with
from utils import response as resp
from flask_jwt_extended import (
    current_user
)

def admin_access(fn):
    @wraps(fn)
    def f_admin_access(*args, **kwargs):
        if current_user['role'] == Role.Admin.value:
            res = fn(*args, **kwargs)
            return res
        return response_with(resp.UNAUTHORIZED_403)
    return f_admin_access