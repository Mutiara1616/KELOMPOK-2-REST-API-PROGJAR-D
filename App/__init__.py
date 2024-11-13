from flask import Flask
from App.extensions import db, api
from App.routes.user_routes import user_bp
from App.routes.matakuliah_routes import matakuliah_bp
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    db.init_app(app)
    api.init_app(app)

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(matakuliah_bp)

    @app.route('/')
    def home():
        return '<h1>Flask REST API Progjar</h1>'

    return app