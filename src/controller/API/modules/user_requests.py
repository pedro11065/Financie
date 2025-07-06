from flask import Blueprint, request, render_template, redirect, session
from flask_login import logout_user, login_required

from src.model.auth.JWT import *

from src.controller.API.resquests_controller import Api_request

#from src import cache

# Tudo aqui é: /user...

user_api_request = Blueprint('auth_user_api', __name__, template_folder='templates', static_folder='static')

# -------------------------------------------------------------------------------------

@user_api_request.route('/login', methods=['GET'])
def login():

    token = request.headers.get('Authorization')
    auth = Auth0() ; payload = auth.decrypt(token)

    api_request = Api_request(payload, request)

    return api_request.user.login()

# -------------------------------------------------------------------------------------

@user_api_request.route('/register', methods=['POST'])
def register():

    token = request.headers.get('Authorization')
    auth = Auth0() ; payload = auth.decrypt(token)

    api_request = Api_request(payload, request)

    return api_request.user.register()

# -------------------------------------------------------------------------------------

@user_api_request.route('/forget-password')
def forget_password():

    token = request.headers.get('Authorization')
    auth = Auth0() ; payload = auth.decrypt(token)

    api_request = Api_request(payload, request)
    
    return api_request.user.forget_password()

# -------------------------------------------------------------------------------------

# @user_request.route('/settings', methods=['GET', 'POST'])
# @login_required
# def settings():
#     if request.method == 'POST':
#         settings = request.get_json()
#         return None #process_settings(settings)
        
#     if request.method == 'GET':
#         cache.delete(f'user_{current_user.id}')
#         return render_template("user/settings.html")

# -------------------------------------------------------------------------------------

# @user_request.route('/logout')
# @login_required
# def logout():
#     cache.delete(f'user_{current_user.id}') # Deletar as entradas relacionadas ao usuário
#     session.clear() # Limpa a sessão
#     logout_user()
#     return redirect('/')  


