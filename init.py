from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()     # shared SQLAlchemy database instance
ma = Marshmallow()    # shared Marshmallow instance
jwt = JWTManager()    # JWT manager (uses JWT_SECRET_KEY from config)
bcrypt = Bcrypt()     # password hashing
