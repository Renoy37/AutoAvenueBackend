from flask import Blueprint, request, jsonify
from models import User
from config import db
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from flask_cors import CORS, cross_origin


auth_bp = Blueprint('auth_bp', __name__)

class Register(Resource):
    @cross_origin(allow_headers=['Content-Type'])
    def post(self):
        try:
            data = request.get_json()

            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            role = data.get('role')

            # Validate input data
            if not username or not email or not password or not role:
                return {'message': 'Missing required fields'}, 400

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return {'message': 'User with this email already exists'}, 400

            user = User(username=username, email=email, role=role)
            user.password_hash = password
            db.session.add(user)
            db.session.commit()

            return {'message': 'User created successfully', 'user': user.to_dict()}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

class Login(Resource):
    @cross_origin(allow_headers=['Content-Type'])
    def post(self):
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            # Validate input data
            if not email or not password:
                return {'message': 'Missing email or password'}, 400

            user = User.query.filter_by(email=email).first()
            if not user or not user.authenticate(password):
                return {'message': 'Invalid email or password'}, 401

            access_token = create_access_token(identity=user.id)
            return {'message': 'Login successful', 'access_token': access_token, 'role': user.role}, 200
        except Exception as e:
            return {'message': str(e)}, 500
