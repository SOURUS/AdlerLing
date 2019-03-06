import functools
from flask import Flask, make_response
from flask_jwt_extended import get_jwt_claims


def check_roles(roles):
    def inside_function(func):
        @functools.wraps(func)
        def decorated_function(*args, **kwargs):
            claims = get_jwt_claims()
            if common_role(claims["roles"], roles):
                func(*args)
            else:
                return make_response("You have no permission for that", 401)
        return decorated_function
    return inside_function


def common_role(a, b):
    a_set = set(a)
    b_set = set(b)
    if a_set & b_set:
        return True
    else:
        return False
