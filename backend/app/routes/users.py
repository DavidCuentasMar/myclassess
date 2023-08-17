from flask import Blueprint

bp = Blueprint('users', __name__)

@bp.route('/')
def index():
    return 'USERS PING'