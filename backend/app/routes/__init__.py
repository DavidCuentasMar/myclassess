from .users import bp as users_bp
from .classes import bp as classes_bp

def init_app(app):
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(classes_bp, url_prefix="/classes")
