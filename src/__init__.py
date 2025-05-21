from flask import Flask
from .controller.user.user_requests import user_api_request

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_api_request, url_prefix='/api/user')  # Fixed leading slash

    return app