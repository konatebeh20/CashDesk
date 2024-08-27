from flask_jwt_extended import jwt_required
from flask import request, jsonify
import uuid
from config.db import db
from model.tt import Item, Formbuying
from werkzeug.security import check_password_hash

@jwt_required()
def SaveItem():
    response = {}
    try:
        # Collecte des données de l'item
        it_name = request.json.get('itemname')
        it_price = request.json.get('price')
        it_description = request.json.get('description')
        it_brand = request.json.get('brand')
        it_barcode = request.json.get('barcode')
        it_stock = request.json.get('stock')
        it_lowstock = request.json.get('lowstock')
        it_uid = str(uuid.uuid4())

        # Création et sauvegarder d'un nouvel item
        new_item = Item(
            it_name=it_name,
            it_price=it_price,
            it_description=it_description,
            it_brand=it_brand,
            it_barcode=it_barcode,
            it_stock=it_stock,
            it_lowstock=it_lowstock,
            it_uid=it_uid
        )
        
        db.session.add(new_item)
        db.session.commit()

        response['status'] = 'Success'
    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return jsonify(response)






































# from flask import request, jsonify
# from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
# from datetime import timedelta
# import uuid
# import bcrypt
# from config.db import db
# from model.tt import Items, Formbuying
# from werkzeug.security import check_password_hash


# @jwt_required()
# def SaveItem():
#     response = {}
#     try:
#         data = request.get_json()
#         it_uid = str(uuid.uuid4())
#         new_items = Items(
#             it_name=data.get('itemname'),
#             it_price=data.get('price'),
#             it_description=data.get('description'),
#             it_brand=data.get('brand'),
#             it_barcode=data.get('barcode'),
#             it_stock=data.get('stock'),
#             it_lowstock=data.get('lowstock'),
#             it_uid=str(uuid.uuid4()),
#         )
        
#         db.session.add(new_items)
#         db.session.commit()

#         return jsonify({'status': 'success', 'message': 'Items created successfully'}), 201

#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400


# @jwt_required()
# def ReadAllItem():
#     try:
#         items = Items.query.all()
#         items_list = [
#             {
#                 'it_uid': items.it_uid,
#                 'name': items.it_name,
#                 'price': items.it_price
#             } for items in items
#         ]
        
#         return jsonify({'status': 'success', 'items': items_list}), 200

#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400


# @jwt_required()
# def UpdateItem():
#     try:
#         data = request.get_json()
#         uid = data.get('it_uid')
#         items = Items.query.filter_by(it_uid=uid).first()

#         if items:
#             items.it_name = data.get('name', items.it_name)
#             items.it_price = data.get('price', items.it_price)
#             items.it_barcode = data.get('barcode', items.it_barcode)
            
#             db.session.commit()

#             return jsonify({'status': 'success', 'message': 'Items updated successfully'}), 200
#         else:
#             return jsonify({'status': 'error', 'message': 'Items not found'}), 404

#     except Exception as e:
#         return jsonify({'status': 'error', 'error_description': str(e)}), 400


