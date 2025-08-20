from lab.lab3.api.main import app  # delegate to package implementation for tests

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
