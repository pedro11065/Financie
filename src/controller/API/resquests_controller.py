from src.model.services.API.user_service import User_service
from src.model.services.API.asset_service import Asset_service
from src.model.services.API.liability_service import Liability_service
from src.model.services.API.transaction_service import Transaction_service

class Api_request:

    def __init__(self, payload, request):
        self.user = User_service(payload, request)
        self.asset = Asset_service(payload, request)
        self.liability = Liability_service(payload, request)
        self.transaction = Transaction_service(payload, request)