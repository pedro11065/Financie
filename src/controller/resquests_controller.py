from src.model.services.user_service import User_service
from src.model.services.asset_service import Asset_service
from src.model.services.liability_service import Liability_service

class Api_request:

    def __init__(self, payload, request):
        self.user = User_service(payload, request)
        self.asset = Asset_service(payload, request)
        self.liability = Liability_service(payload, request)