from flask import Flask

from appv.config import app_config

from appv.api.offers import offers


def create_app():
    app_ = Flask(__name__)
    return app_


app = create_app()
app.config.from_object(app_config["development"])
app.register_blueprint(offers)
