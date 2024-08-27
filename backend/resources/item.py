from flask import request, jsonify
from flask_restful import Resource
from model.tt import Item, db
from flask_jwt_extended import jwt_required

class ItemApi(Resource):
    @jwt_required()
    def get(self, route):
        if route == 'all':
            items = Item.query.all()
            return jsonify([item.to_dict() for item in items])
        elif route == 'one':
            item_id = request.args.get('id')
            item = Item.query.get(item_id)
            return jsonify(item.to_dict() if item else {})

    @jwt_required()
    def post(self, route):
        if route == 'add':
            data = request.get_json()
            new_item = Item(
                it_name=data['it_name'],
                it_description=data['it_description'],
                it_price=data['it_price'],
                it_brand=data['it_brand'],
                it_barcode=data['it_barcode'],
                it_stock=data['it_stock'],
                it_lowstock=data['it_lowstock'],
                it_uid=data['it_uid']
            )
            db.session.add(new_item)
            db.session.commit()
            return jsonify({'message': 'Item ajouté avec succès'}), 201

    # Méthodes pour DELETE et PATCH