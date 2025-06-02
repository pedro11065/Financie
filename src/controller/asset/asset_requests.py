from flask import Blueprint, request, render_template, redirect, session
from flask_login import logout_user, login_required

from src.controller.resquests import Api_request

#from src import cache

# Tudo aqui é: /user...

asset_api_request = Blueprint('auth_asset_api', __name__, template_folder='templates', static_folder='static')

# -------------------------------------------------------------------------------------

@asset_api_request.route('/create', methods=['POST'])
def create():
    data = request.get_json() ; api_request = Api_request()
    return api_request.asset.create(data)

# -------------------------------------------------------------------------------------

# @user_api_request.route(f'/{id}', methods=['POST'])
# def register():
#     data = request.get_json() ; api_request = Api_request()
#     return api_request.user.register(data)

# # -------------------------------------------------------------------------------------

# @user_api_request.route(f'/edit/{id}')
# def forget_password():
#     data = request.get_json() ; api_request = Api_request()
#     return api_request.user.forget_password(data)



