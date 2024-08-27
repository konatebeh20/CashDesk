from flask import request, jsonify
from flask_jwt_extended import create_access_token
from datetime import timedelta
import uuid
import bcrypt
from config.db import db
from model.tt import Admin

def create_admin():
    try:
        data = request.get_json()
        ad_uid = str(uuid.uuid4())
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        
        new_admin = Admin(
            ad_fullname=data['fullname'],
            ad_username=data['username'],
            ad_mobile=data['mobile'],
            ad_address=data['address'],
            ad_email=data['email'],
            ad_password=hashed_password,
            ad_uid=ad_uid
        )
        
        db.session.add(new_admin)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'Admin created successfully'}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'error_description': str(e)}), 400

def read_all_admin():
    try:
        admins = Admin.query.all()
        admin_list = [{
            'ad_uid': admin.ad_uid,
            'fullname': admin.ad_fullname,
        } for admin in admins]
        return jsonify({'status': 'success', 'admins': admin_list}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'error_description': str(e)}), 400

def read_single_admin(ad_uid):
    try:
        admin = Admin.query.filter_by(ad_uid=ad_uid).first()
        if admin:
            admin_info = {
                'ad_uid': admin.ad_uid,
                'fullname': admin.ad_fullname,
                'username': admin.ad_username,
                'mobile': admin.ad_mobile,
                'address': admin.ad_address,
                'email': admin.ad_email,
            }
            return jsonify({'status': 'success', 'admin': admin_info}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Admin not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'error_description': str(e)}), 400

def update_admin(ad_uid):
    try:
        admin = Admin.query.filter_by(ad_uid=ad_uid).first()
        if admin:
            data = request.get_json()
            admin.ad_fullname = data.get('fullname', admin.ad_fullname)
            admin.ad_username = data.get('username', admin.ad_username)
            admin.ad_mobile = data.get('mobile', admin.ad_mobile)
            admin.ad_address = data.get('address', admin.ad_address)
            admin.ad_email = data.get('email', admin.ad_email)
            if 'password' in data:
                admin.ad_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Admin updated successfully'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Admin not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'error_description': str(e)}), 400

def delete_admin(ad_uid):
    try:
        admin = Admin.query.filter_by(ad_uid=ad_uid).first()
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Admin deleted successfully'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Admin not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'error_description': str(e)}), 400

def login_admin():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        admin = Admin.query.filter_by(ad_username=username).first()

        if admin and bcrypt.checkpw(password.encode('utf-8'), admin.ad_password.encode('utf-8')):
            expires = timedelta(hours=1)
            access_token = create_access_token(identity=username, expires_delta=expires)
            return jsonify({'status': 'success', 'message': 'Login successful', 'access_token': access_token}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'status': 'error', 'error_description': str(e)}), 400