from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/v1/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    return jsonify({'cart_id': 1, 'items': [data]}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
