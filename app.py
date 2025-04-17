from flask import Flask
from auth import auth_bp
# from usuarios import usuarios_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
# app.register_blueprint(usuarios_bp)

# Esto solo se ejecuta si corres app.py directamente (en desarrollo)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
