from flask import Flask, jsonify, request
from flask_cors import CORS
from app import consulter_stock_central, generer_rapport_consolide, synchroniser_stock

app = Flask(__name__)
CORS(app)

# Endpoint: Consulter le stock d’un magasin
@app.route('/api/v1/stores/<int:magasin_id>/stock', methods=['GET'])
def get_stock_magasin(magasin_id):
    # À adapter pour stock magasin spécifique
    stock = consulter_stock_central()  # Prototype: retourne le stock central
    return jsonify({'stock': stock}), 200

# Endpoint: Générer un rapport consolidé des ventes
@app.route('/api/v1/report', methods=['GET'])
def get_rapport():
    rapport = generer_rapport_consolide()
    return jsonify({'rapport': rapport}), 200

# Endpoint: Mettre à jour un produit
@app.route('/api/v1/products/<int:produit_id>', methods=['PUT'])
def update_produit(produit_id):
    data = request.json
    # À compléter: mise à jour du produit dans la base
    return jsonify({'produit': {'id': produit_id, **data}}), 200

# Endpoint: Visualiser les performances globales
@app.route('/api/v1/dashboard', methods=['GET'])
def get_dashboard():
    # À compléter: indicateurs clés
    indicateurs = []
    return jsonify({'indicateurs': indicateurs}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
