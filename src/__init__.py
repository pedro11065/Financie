from flask import Flask
from .controller.web.modules.index_requests import index

from .controller.API.modules.user_requests import user_api_request
from .controller.API.modules.asset_requests import asset_api_request
from .controller.API.modules.liabilities_requests import liability_api_request
from .controller.API.modules.transactions_requests import transaction_api_request

def create_app():
    app = Flask(__name__, static_folder='view/static', template_folder='view/templates')

    #WEB
    app.register_blueprint(index, url_prefix='/home' and '/')

    #API
    app.register_blueprint(user_api_request, url_prefix='/api/user') 
    app.register_blueprint(asset_api_request, url_prefix='/api/asset') 
    app.register_blueprint(liability_api_request, url_prefix='/api/liability') 
    app.register_blueprint(transaction_api_request, url_prefix='/api/transaction') 

    return app