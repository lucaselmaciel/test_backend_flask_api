from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_class)
    db.init_app(app)

    return app


app = create_app()
with app.app_context():
    from app import errors
    from .controllers import comments, posts, users

    app.register_blueprint(errors.BLUEPRINT)
    app.register_blueprint(posts.BLUEPRINT)
    app.register_blueprint(comments.BLUEPRINT)
    app.register_blueprint(users.BLUEPRINT)
