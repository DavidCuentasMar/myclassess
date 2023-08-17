from flask import Flask
from .extensions import db

def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@postgres:5432/postgresdb"
    
    db.init_app(app)

    from . import routes
    routes.init_app(app)
    
    return app

app = create_app()