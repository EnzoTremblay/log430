from lab.lab3.api.main import app  # delegate to package implementation for tests

if __name__ == '__main__':
    import os
    port = int(os.getenv('PORT', '5000'))
    app.run(host='0.0.0.0', port=port)
