from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash

app = Flask(__name__)
CORS(app)

# Configuration de la base de données
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'votre_utilisateur'
app.config['MYSQL_PASSWORD'] = 'votre_mot_de_passe'
app.config['MYSQL_DB'] = 'nom_de_votre_base_de_donnees'

mysql = MySQL(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()

    if user and check_password_hash(user['password'], password):
        return jsonify({"message": "Connexion réussie"}), 200
    else:
        return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401

if __name__ == '__main__':
    app.run(debug=True)
