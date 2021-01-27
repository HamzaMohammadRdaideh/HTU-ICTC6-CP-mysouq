import os
from flask import Flask
from mongoengine import *
from capstone.models import *
import json

def create_app(test_config=None):
    # create the Flask
    app = Flask(__name__, instance_relative_config=True)

    # configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGO_URI="mongodb://root:example@localhost:27017/blog?authSource=admin"
    )

    # connect to MongoDB using mongoengine
    connect(
        db='capstone',
        username='root',
        password='example',
        authentication_source='admin'
    )

  # register the 'login' blueprint
    from .blueprints.login import login_bp
    app.register_blueprint(login_bp)

    # register the 'user' blueprint
    from .blueprints.signup import signup_bp
    app.register_blueprint(signup_bp)

    # register the 'user' blueprint
    from .blueprints.home import home_bp
    app.register_blueprint(home_bp)

   # register the 'user' blueprint
    from .blueprints.user import user_bp
    app.register_blueprint(user_bp)

    return app

