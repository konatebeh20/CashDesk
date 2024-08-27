from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
import uuid
import bcrypt
from config.db import db
from model.tt import User

# Function to create a new user
def create_user():
    response = {}
    try:
        data = request.get_json()
        ad_uid = str(uuid.uuid4())
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        new_user = User(
            ad_fullname=data['fullname'],
            ad_username=data['username'],
            ad_mobile=data['mobile'],
            ad_address=data['address'],
            ad_email=data['email'],
            ad_password=hashed_password,
            ad_uid=ad_uid
        )

        db.session.add(new_user)
        db.session.commit()

        response['status'] = 'success'
        response['message'] = 'User created successfully'
        return jsonify(response), 201
    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)
        return jsonify(response), 400

# Function to get all users
@jwt_required()
def read_all_user():
    response = {}
    try:
        users = User.query.all()
        user_list = [{
            'ad_uid': user.ad_uid,
            'fullname': user.ad_fullname,
        } for user in users]

        response['status'] = 'success'
        response['user'] = user_list
        return jsonify(response), 200
    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)
        return jsonify(response), 400

# Function to get a single user by UID
@jwt_required()
def read_single_user(ad_uid):
    response = {}
    try:
        user = User.query.filter_by(ad_uid=ad_uid).first()
        if user:
            user_info = {
                'ad_uid': user.ad_uid,
                'fullname': user.ad_fullname,
                'username': user.ad_username,
                'mobile': user.ad_mobile,
                'address': user.ad_address,
                'email': user.ad_email,
            }
            response['status'] = 'success'
            response['User'] = user_info
            return jsonify(response), 200
        else:
            response['status'] = 'error'
            response['message'] = 'User not found'
            return jsonify(response), 404
    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)
        return jsonify(response), 400

# Function to update a user
@jwt_required()
def update_user(ad_uid):
    response = {}
    try:
        user = User.query.filter_by(ad_uid=ad_uid).first()
        if user:
            data = request.get_json()
            user.ad_fullname = data.get('fullname', user.ad_fullname)
            user.ad_username = data.get('username', user.ad_username)
            user.ad_mobile = data.get('mobile', user.ad_mobile)
            user.ad_address = data.get('address', user.ad_address)
            user.ad_email = data.get('email', user.ad_email)
            if 'password' in data:
                user.ad_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

            db.session.commit()
            response['status'] = 'success'
            response['message'] = 'User updated successfully'
            return jsonify(response), 200
        else:
            response['status'] = 'error'
            response['message'] = 'User not found'
            return jsonify(response), 404
    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)
        return jsonify(response), 400

# Function to delete a user
@jwt_required()
def delete_user(ad_uid):
    response = {}
    try:
        user = User.query.filter_by(ad_uid=ad_uid).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            response['status'] = 'success'
            response['message'] = 'User deleted successfully'
            return jsonify(response), 200
        else:
            response['status'] = 'error'
            response['message'] = 'User not found'
            return jsonify(response), 400
    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)
        return jsonify(response), 400
































































































































































































































































































































































































































































# from flask import request, jsonify
# from flask_jwt_extended import create_access_token, jwt_required
# from datetime import timedelta
# import uuid
# import bcrypt
# from config.db import db
# from model.tt import User

# # Function to create a new user
# def create_user():
#     try:
#         data = request.get_json()
#         ad_uid = str(uuid.uuid4())
#         hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        
#         new_user = User(
#             ad_fullname=data['fullname'],
#             ad_username=data['username'],
#             ad_mobile=data['mobile'],
#             ad_address=data['address'],
#             ad_email=data['email'],
#             ad_password=hashed_password,
#             ad_uid=ad_uid
#         )
        
#         db.session.add(new_user)
#         db.session.commit()

#         return jsonify({'status': 'success', 'message': 'User created successfully'}), 201
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# # Function to get all users
# @jwt_required()
# def read_all_user():
#     try:
#         users = User.query.all()
#         user_list = [{
#             'ad_uid': user.ad_uid,
#             'fullname': user.ad_fullname,
#         } for user in users]
#         return jsonify({'status': 'success', 'user': user_list}), 200
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# # Function to get a single user by UID
# @jwt_required()
# def read_single_user(ad_uid):
#     try:
#         user = User.query.filter_by(ad_uid=ad_uid).first()
#         if user:
#             user_info = {
#                 'ad_uid': user.ad_uid,
#                 'fullname': user.ad_fullname,
#                 'username': user.ad_username,
#                 'mobile': user.ad_mobile,
#                 'address': user.ad_address,
#                 'email': user.ad_email,
#             }
#             return jsonify({'status': 'success', 'User': user_info}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'User not found'}), 404
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# # Function to update a user
# @jwt_required()
# def update_user(ad_uid):
#     try:
#         user = User.query.filter_by(ad_uid=ad_uid).first()
#         if user:
#             data = request.get_json()
#             user.ad_fullname = data.get('fullname', user.ad_fullname)
#             user.ad_username = data.get('username', user.ad_username)
#             user.ad_mobile = data.get('mobile', user.ad_mobile)
#             user.ad_address = data.get('address', user.ad_address)
#             user.ad_email = data.get('email', user.ad_email)
#             if 'password' in data:
#                 user.ad_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
#             db.session.commit()
#             return jsonify({'status': 'success', 'message': 'User updated successfully'}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'User not found'}), 404
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# # Function to delete a user
# @jwt_required()
# def delete_user(ad_uid):
#     try:
#         user = User.query.filter_by(ad_uid=ad_uid).first()
#         if user:
#             db.session.delete(user)
#             db.session.commit()
#             return jsonify({'status': 'success', 'message': 'User deleted successfully'}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'User not found'}), 404
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# # Function to login a user and return a JWT token
# def login_user():
#     try:
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')

#         user = User.query.filter_by(ad_username=username).first()

#         if user and bcrypt.checkpw(password.encode('utf-8'), user.ad_password.encode('utf-8')):
#             expires = timedelta(hours=1)
#             access_token = create_access_token(identity=username, expires_delta=expires)
#             return jsonify({'status': 'success', 'message': 'Login successful', 'access_token': access_token}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400












# from flask import request, jsonify
# from flask_jwt_extended import create_access_token
# from datetime import timedelta
# import uuid
# import bcrypt
# from config.db import db
# from model.tt import User

# def create_user():
#     try:
#         data = request.get_json()
#         ad_uid = str(uuid.uuid4())
#         hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        
#         new_user = User(
#             ad_fullname=data['fullname'],
#             ad_username=data['username'],
#             ad_mobile=data['mobile'],
#             ad_address=data['address'],
#             ad_email=data['email'],
#             ad_password=hashed_password,
#             ad_uid=ad_uid
#         )
        
#         db.session.add(new_user)
#         db.session.commit()

#         return jsonify({'status': 'success', 'message': 'User created successfully'}), 201
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# def read_all_user():
#     try:
#         user = User.query.all()
#         user_list = [{
#             'ad_uid': user.ad_uid,
#             'fullname': user.ad_fullname,
#         } for user in user]
#         return jsonify({'status': 'success', 'user': user_list}), 200
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# def read_single_user(ad_uid):
#     try:
#         user = User.query.filter_by(ad_uid=ad_uid).first()
#         if user:
#             user_info = {
#                 'ad_uid': user.ad_uid,
#                 'fullname': user.ad_fullname,
#                 'username': user.ad_username,
#                 'mobile': user.ad_mobile,
#                 'address': user.ad_address,
#                 'email': user.ad_email,
#             }
#             return jsonify({'status': 'success', 'User': user_info}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'User not found'}), 404
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# def update_user(ad_uid):
#     try:
#         user = User.query.filter_by(ad_uid=ad_uid).first()
#         if user:
#             data = request.get_json()
#             user.ad_fullname = data.get('fullname', user.ad_fullname)
#             user.ad_username = data.get('username', user.ad_username)
#             user.ad_mobile = data.get('mobile', user.ad_mobile)
#             user.ad_address = data.get('address', user.ad_address)
#             user.ad_email = data.get('email', user.ad_email)
#             if 'password' in data:
#                 user.ad_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
#             db.session.commit()
#             return jsonify({'status': 'success', 'message': 'User updated successfully'}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'User not found'}), 404
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# def delete_user(ad_uid):
#     try:
#         user = User.query.filter_by(ad_uid=ad_uid).first()
#         if user:
#             db.session.delete(user)
#             db.session.commit()
#             return jsonify({'status': 'success', 'message': 'User deleted successfully'}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'User not found'}), 404
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400

# def login_user():
#     try:
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')

#         user = User.query.filter_by(ad_username=username).first()

#         if user and bcrypt.checkpw(password.encode('utf-8'), user.ad_password.encode('utf-8')):
#             expires = timedelta(hours=1)
#             access_token = create_access_token(identity=username, expires_delta=expires)
#             return jsonify({'status': 'success', 'message': 'Login successful', 'access_token': access_token}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401
#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400