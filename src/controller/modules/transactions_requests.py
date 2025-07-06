from flask import Blueprint, request, render_template, redirect, session, jsonify
from flask_login import logout_user, login_required

from src.controller.resquests_controller import Api_request
from src.model.auth.JWT import *

transaction_api_request = Blueprint('auth_transaction_api', __name__, template_folder='templates', static_folder='static')

# -------------------------------------------------------------------------------------
@login_required
@transaction_api_request.route('/create', methods=['POST'])
def create():

    token = request.headers.get('Authorization')
    auth = Auth0() ; payload = auth.decrypt(token)

    api_request = Api_request(payload, request)

    return api_request.transaction.create() 

# -------------------------------------------------------------------------------------
@login_required
@transaction_api_request.route(f'/id', methods=['GET'])
def search():

    token = request.headers.get('Authorization')
    auth = Auth0() ; payload = auth.decrypt(token)

    api_request = Api_request(payload, request)

    return api_request.transaction.search()

# -------------------------------------------------------------------------------------
@login_required
@transaction_api_request.route(f'/update', methods=['PUT'])
def update():

    token = request.headers.get('Authorization')
    auth = Auth0() ; payload = auth.decrypt(token)

    api_request = Api_request(payload, request)

    return api_request.transaction.update()

# -------------------------------------------------------------------------------------
@login_required
@transaction_api_request.route(f'/delete', methods=['DELETE'])
def delete():

    token = request.headers.get('Authorization')
    auth = Auth0() ; payload = auth.decrypt(token)

    api_request = Api_request(payload, request)

    return api_request.transaction.delete()
