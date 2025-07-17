from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/v1/clients', methods=['POST'])
def create_client():
    data = request.json
    return jsonify({'id': 1, **data}), 201

if __name__ == '__main__':
    app.run(port=5004)
