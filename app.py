from flask import Flask
from auth import auth_bp
# from usuarios import usuarios_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
# app.register_blueprint(usuarios_bp)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
