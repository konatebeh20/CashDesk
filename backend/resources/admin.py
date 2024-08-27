from flask import request, jsonify
from flask_restful import Resource
from model.tt import Admin, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

class AdminApi(Resource):
    @jwt_required()
    def get(self, route):
        if route == 'all':
            admins = Admin.query.all()
            return jsonify([admin.to_dict() for admin in admins])
        elif route == 'one':
            admin_id = request.args.get('id')
            admin = Admin.query.get(admin_id)
            return jsonify(admin.to_dict() if admin else {})

    @jwt_required()
    def post(self, route):
        if route == 'add':
            data = request.get_json()
            new_admin = Admin(
                ad_fullname=data['ad_fullname'],
                ad_username=data['ad_username'],
                ad_mobile=data['ad_mobile'],
                ad_address=data['ad_address'],
                ad_email=data['ad_email'],
                ad_password=generate_password_hash(data['ad_password']),
                ad_uid=data['ad_uid']
            )
            db.session.add(new_admin)
            db.session.commit()
            return jsonify({'message': 'Admin ajouté avec succès'}), 201

    # Méthodes pour DELETE et PATCH si applicable