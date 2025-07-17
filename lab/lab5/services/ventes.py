from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/v1/sales', methods=['GET'])
def get_sales():
    return jsonify([{'id': 1, 'total': 100.0}, {'id': 2, 'total': 50.0}])

if __name__ == '__main__':
    app.run(port=5002)
