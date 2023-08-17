from flask import Blueprint

bp = Blueprint('classes', __name__)

@bp.route('/')
def index():
    return 'CLASSES PING'