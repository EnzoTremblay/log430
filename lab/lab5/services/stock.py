from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/v1/stock', methods=['GET'])
def get_stock():
    return jsonify([{'produit': 'Outil', 'quantite': 100}, {'produit': 'Stylo', 'quantite': 200}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
