from flask import Blueprint

# Create blueprints for each set of routes
bp = Blueprint('product_routes', __name__)
bp = Blueprint('auth_routes', __name__)
bp = Blueprint('cart_routes', __name__)

# Import route modules
from . import product_routes
from . import auth_routes
from . import cart_routes
