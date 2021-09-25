from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing the flask extentions
    bootstrap.init_app(app)

    # Registering the blueprint

    from . main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return(app)