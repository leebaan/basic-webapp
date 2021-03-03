from flask import Flask
from .routes import main


def create_app():
    '''Application Factory - set up application'''
    app = Flask(__name__)
    app.register_blueprint(main)

    return app

if __name__ == "__main__":
    a = create_app()
    a.run()