from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db import db
from flask_jwt_extended import JWTManager
from sqlalchemy import text
import models
import os

from resources.classeController import blp as ClasseBlueprint
from resources.genreController import blp as GenreBlueprint
from resources.livreController import blp as LivreBlueprint
from resources.auteurController import blp as AuteurBlueprint
from resources.adherentController import blp as AdherentBlueprint
from resources.empruntController import blp as EmpruntBlueprint
def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Bibliotheque REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)
    db.init_app(app)
    api = Api(app)
    migrate = Migrate(app, db)
   
    with app.app_context():
        db.create_all()
    
    @app.route('/test_db')
    def test_db():
        try:
            result = db.session.execute(text('SELECT 1'))
            return "Database connection successful!"
        except Exception as e:
            return f"Database connection failed: {e}"

    api.register_blueprint(ClasseBlueprint)
    api.register_blueprint(GenreBlueprint)
    api.register_blueprint(LivreBlueprint)
    api.register_blueprint(AuteurBlueprint)
    api.register_blueprint(AdherentBlueprint)
    api.register_blueprint(EmpruntBlueprint)
    return app
