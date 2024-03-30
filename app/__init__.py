from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_smorest import Api

# Import configuration settings
from config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
api = Api(app)

# Import models
from app.models import User, Product, Cart

# Import routes
from app.routes import product_routes, auth_routes, cart_routes

# Import schemas
from app.schemas import UserSchema, ProductSchema, CartSchema

# Register routes
app.register_blueprint(product_routes.bp)
app.register_blueprint(auth_routes.bp)
app.register_blueprint(cart_routes.bp)

# Define Marshmallow schemas
user_schema = UserSchema()
product_schema = ProductSchema()
cart_schema = CartSchema()

if __name__ == '__main__':
    app.run()
