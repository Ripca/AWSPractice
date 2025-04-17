from flask import Blueprint, render_template, request
import requests

auth_bp = Blueprint('auth', __name__)
API_GATEWAY_URL = 'https://4x3ojau8ec.execute-api.us-east-1.amazonaws.com/user'  # Sustituye con el real

@auth_bp.route('/')
def login():
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if not username or not password:
        return render_template('login.html', message="Faltan datos")

    try:
        response = requests.post(API_GATEWAY_URL, json={"username": username, "password": password})
        if response.status_code == 200:
            return render_template('login.html', message="Usuario registrado")
        else:
            return render_template('login.html', message="Error al registrar")
    except Exception as e:
        return render_template('login.html', message=f"Error: {e}")
