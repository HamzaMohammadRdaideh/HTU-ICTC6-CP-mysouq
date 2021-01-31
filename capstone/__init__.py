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
        MONGO_URI="mongodb://root:example@localhost:27017/capstone?authSource=admin"
    )

    # connect to MongoDB using mongoengine
    connect(
        db='capstone',
        username='root',
        password='example',
        authentication_source='admin'
    )


    @app.route('/init-db')
    def init_db():
        
        common_password = pbkdf2_sha256.hash('1234')

        user_1 = User(username='Admin',password = common_password , birthday = "2009-12-30 14:09:01" , email = 'aaa@gmail.com' , role = 2 , first_name='Admin', last_name='Admin').save()

        user_2 = User(username='hamza_96',password = common_password , birthday = "2009-12-30 14:09:01" , email = 'aaa@gmail.com' , role = 0 , first_name='hamza', last_name='rdaideh').save()

        user_3 = User(username='reema_95',password = common_password , birthday = "2009-12-30 14:09:01" , email = 'aaa@gmail.com' , role = 0, first_name='Admin', last_name='eilouti').save()

        user_4 = User(username='hesham_94',password = common_password , birthday = "2009-12-30 14:09:01" , email = 'aaa@gmail.com' , role = 0, first_name='hesham', last_name='marei').save()

        user_5 = User(username='disable',password = common_password , birthday = "2009-12-30 14:09:01" , email = 'aaa@gmail.com' , role = 0, first_name='disable', last_name='disable' , disable = True).save()


        item_1 = Item(title = "First", description = 'First' ,date = "2009-12-30 14:09:01", price = "0" , category = "clothes").save()

        item_2 = Item(title = "Sec" , description = 'First' ,date = "2020-12-30 14:09:01", price = "0" , category = "clothes").save()

        item_3 = Item(title = "Third", description = 'First' ,date = "2011-12-30 14:09:01", price = "0" , category = "clothes").save()

        return "Database initialized :)!"



  # register the 'login' blueprint
    from .blueprints.login import login_bp
    app.register_blueprint(login_bp)

    # register the 'signup' blueprint
    from .blueprints.signup import signup_bp
    app.register_blueprint(signup_bp)

    # register the 'home' blueprint
    from .blueprints.home import home_bp
    app.register_blueprint(home_bp)

   # register the 'user' blueprint
    from .blueprints.user import user_bp
    app.register_blueprint(user_bp)
 
 # register the 'user' blueprint
    from .blueprints.profile import profile_bp
    app.register_blueprint(profile_bp)

    return app

