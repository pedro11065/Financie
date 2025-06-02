from src.controller.user.user_processing import User_api_process
from src.controller.asset.asset_processing import Asset_api_process

class Api_request:

    def __init__(self):
        self.user = User_api_process()
        self.asset= Asset_api_process()