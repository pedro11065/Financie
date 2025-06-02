from flask import Flask
from .controller.user.user_requests import user_api_request
from .controller.asset.asset_requests import asset_api_request

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_api_request, url_prefix='/api/user') 
    app.register_blueprint(asset_api_request, url_prefix='/api/asset') 

    return app