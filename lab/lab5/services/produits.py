from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify([{'id': 1, 'nom': 'Outil', 'prix': 10.0}, {'id': 2, 'nom': 'Stylo', 'prix': 1.5}])

@app.route('/api/v1/products/<int:produit_id>', methods=['PUT'])
def update_product(produit_id):
    data = request.json
    return jsonify({'id': produit_id, **data})

if __name__ == '__main__':
    app.run(port=5001)
