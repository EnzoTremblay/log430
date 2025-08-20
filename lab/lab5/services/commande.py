from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/v1/checkout', methods=['POST'])
def checkout():
    data = request.json
    return jsonify({'order_id': 1, 'status': 'validated', 'details': data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
