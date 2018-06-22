from flask import Flask
# from flask_restful import Api
from appv.config import app_config

def create_app():
    # Initialize flask app
    app_ = Flask(__name__)

    return app_


app = create_app()
# load from config.py in root folder
app.config.from_object(app_config["development"])
from appv.api.offers import offers
app.register_blueprint(offers)

# from .api.user import user
# app.register_blueprint(user)
# from .api.request import request
# app.register_blueprint(request)