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

@asset_api_request.route(f'/id', methods=['GET'])
def register():
    id = request.args.get('id') ;  type = request.args.get('type') ; api_request = Api_request()
    return api_request.asset.search_by_id(id, type)


