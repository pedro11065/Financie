from src.model.services.user_service import User_api_process
from src.model.services.asset_service import Asset_api_process

class Api_request:

    def __init__(self, payload, request):
        self.user = User_api_process(payload, request)
        self.asset = Asset_api_process(payload, request)