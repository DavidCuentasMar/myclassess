from flask import Blueprint
from ..models.users import Users

bp = Blueprint('users', __name__)

@bp.route('/')
def index():
    return 'USERS PING'

@bp.route('/get_email_by_id/<id>')
def get_user(id):
    user = Users.query.filter_by(id=id).first()
    return {'user': user.email}