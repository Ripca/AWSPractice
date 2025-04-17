# showUsers.py
from flask import Blueprint, render_template
import requests

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def show_users():
    try:
        # URL de tu API Gateway
        api_url = 'https://4x3ojau8ec.execute-api.us-east-1.amazonaws.com/showUsers'
        response = requests.get(api_url)
        data = response.json()

        # Se espera que el API retorne un JSON con una clave 'users'
        users = data.get('users', [])
    except Exception as e:
        # Si algo sale mal, puedes mostrar un mensaje o usar datos de prueba
        users = []
        print(f'Error al obtener los datos: {e}')

    return render_template('users.html', users=users)
