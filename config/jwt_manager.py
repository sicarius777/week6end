from flask_jwt_extended import JWTManager, jwt_refresh_token_required, create_access_token, create_refresh_token

# Initialize Flask app
app = Flask(__name__)

# Configure JWT settings
app.config['JWT_SECRET_KEY'] = 'your_secret_key' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30) 

# Initialize JWTManager
jwt = JWTManager(app)

# Route for token refreshing
@app.route('/refresh_token', methods=['POST'])
@jwt_refresh_token_required()
def refresh_token():
    current_user_id = get_jwt_identity()
    access_token = create_access_token(identity=current_user_id)
    return jsonify(access_token=access_token), 200
