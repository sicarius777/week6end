import os

class Config:
    # Flask app configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    DEBUG = True

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = False  # Token expiration disabled for testing purposes

    # Swagger settings
    API_TITLE = 'E-Commerce API'
    API_VERSION = '1.0'
    OPENAPI_VERSION = '3.0.3'
    SWAGGER_UI_OAUTH_CLIENT_ID = 'swagger-ui'
    SWAGGER_UI_OAUTH_REALM = 'auth-realm'
    SWAGGER_UI_CONFIGURATION = {
        'oauth': {
            'clientId': SWAGGER_UI_OAUTH_CLIENT_ID,
            'realm': SWAGGER_UI_OAUTH_REALM,
            'appName': 'Swagger'
        }
    }
