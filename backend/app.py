from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from config import *
from config.db import db
from config.constant import *
from resources.admin import AdminApi
from resources.user import UserApi
from resources.item import ItemApi
from model.tt import *
from alembic import *
from sqlalchemy import *

app = Flask(__name__)
CORS(app)

# Configuration
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.secret_key = os.urandom(24)
app.config['DEBUG'] = True

# Importation du lien de base de données depuis config/constants.py
app.config['SQLALCHEMY_DATABASE_URI'] = LIEN_BASE_DE_DONNEES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation des extensions
jwt = JWTManager(app)
# db.init_app(app)
db = SQLAlchemy(app)

# Initialisation de Flask-Migrate
migrate = Migrate(app, db)

api = Api(app)

# Ajout des ressources API
api.add_resource(AdminApi, '/api/admin/<string:route>', endpoint='all_admin', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(UserApi, '/api/user/<string:route>', endpoint='all_user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(ItemApi, '/api/item/<string:route>', endpoint='all_item', methods=['GET', 'POST', 'DELETE', 'PATCH'])

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")