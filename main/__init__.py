from flask import Flask


def create_app(test_config=None):


    # create flask app
    app = Flask(__name__)

    app.config.from_object('config.Config')




    return app