# import os

from flask import Flask, jsonify
from init import db, ma, jwt, bcrypt

def create_app():
    """Creates Flask app, loads env config (DATABASE_URI and JWT_SECRET_KEY),
    then registers CLI and route blueprints."""
    app = Flask(__name__)

    app.config.from_object("config.app_config")
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")

    app.json.sort_keys = False  # To keep order of keys in JSON response (as defined in schema)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # CLI commands: flask db create/drop/seed
    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    # Import controllers to activate Blueprints
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app
