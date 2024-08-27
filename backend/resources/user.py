from flask import request, jsonify
from flask_restful import Resource
from model.tt import User, db
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

class UserApi(Resource):
    @jwt_required()
    def get(self, route):
        if route == 'all':
            users = User.query.all()
            return jsonify([user.to_dict() for user in users])
        elif route == 'one':
            user_id = request.args.get('id')
            user = User.query.get(user_id)
            return jsonify(user.to_dict() if user else {})

    def post(self, route):
        if route == 'add':
            data = request.get_json()
            new_user = User(
                ad_fullname=data['ad_fullname'],
                ad_username=data['ad_username'],
                ad_mobile=data['ad_mobile'],
                ad_address=data['ad_address'],
                ad_email=data['ad_email'],
                ad_password=generate_password_hash(data['ad_password']),
                ad_uid=data['ad_uid']
            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'Utilisateur ajouté avec succès'}), 201
        elif route == 'login':
            data = request.get_json()
            user = User.query.filter_by(ad_username=data['username']).first()
            if user and check_password_hash(user.ad_password, data['password']):
                access_token = create_access_token(identity=user.id)
                return jsonify(access_token=access_token), 200
            return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401

    # Méthodes pour DELETE et PATCH