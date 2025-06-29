from flask import Blueprint, request, render_template, redirect, session, jsonify
from flask_login import logout_user, login_required

from src.controller.resquests import Api_request
from src.settings.security.auth0 import *

import os
asset_api_request = Blueprint('auth_asset_api', __name__, template_folder='templates', static_folder='static')

# -------------------------------------------------------------------------------------

@asset_api_request.route('/create', methods=['POST'])
def create():

    token = request.headers.get('Authorization')

    auth = Auth0()
    payload = auth.decrypt(token)

    api_request = Api_request()

    return api_request.asset.create(payload, request) 

# -------------------------------------------------------------------------------------

@asset_api_request.route(f'/id', methods=['GET'])
def search():

    token = request.headers.get('Authorization')

    auth = Auth0() 
    payload = auth.decrypt(token)

    api_request = Api_request()

    return api_request.asset.search(payload, request)
