from flask import Blueprint, jsonify, request # type: ignore
from flask_jwt_extended import create_access_token, create_refresh_token # type: ignore
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = User.get_user_by_name(username = data.get('username'))
    
    if user is not None:
        return jsonify({'error': 'Username already exists'}), 403
    
    new_user = User(
        username = data.get('username'),
        email = data.get('email'),
    )
    
    new_user.set_password(password = data.get('password'))
    
    new_user.save()
    
    
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.get_user_by_name(username = data.get('username'))
    
    if user and (user.check_password(password = data.get('password'))):
        access_token = create_access_token(identity = user.username)
        refresh_token = create_refresh_token(identity = user.username)
        
        return jsonify(
            {
                'message': 'Logged in successfully',
                'tokens' : {
                    'access': access_token,
                    'refresh': refresh_token
                }
            }
        ), 200
    return jsonify({'error': 'Invalid username or password'}), 401    