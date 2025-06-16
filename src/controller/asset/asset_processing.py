from src.model.db import Db
from src.settings.security.auth0 import Auth0
import bcrypt, traceback, uuid, os

from datetime import datetime

from src.model.asset.asset import *

class Asset_api_process:

    def __init__(self):
        self.db = Db("assets")


    # ==============================================================================

    def create(self, data):

        asset = Asset(name=data["name"], 
            description=data["description"], 
            category=data["category"],
            status=data["status"],
            location=data["location"], 
            user_id=data["user_id"],
            created_at=datetime.now(),
            id=uuid.uuid4())
        
        if self.db.assets.create.asset(asset):
            return {"status": True, "message":"Asset created successfully!"}, 201
        else:
            return {"status": False, "message":"Internal server error."}, 500
        
    
     # ==============================================================================


    def search(self, id, type):
        
        if type == "id":

            asset = self.db.assets.search.by_id(id)

            if asset:
                asset.created_at = asset.created_at.strftime('%Y-%m-%d %H:%M:%S')
                asset.updated_at = asset.updated_at.strftime('%Y-%m-%d %H:%M:%S')

                asset = asset.__dict__

                return {"status": True, "data": asset}, 200
            
    #-------------------------------------------------------------------------------

        else:

            assets = self.db.assets.search.by_user_id(id)

            if assets:
                for i, asset in enumerate(assets):
                    asset.created_at = asset.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    asset.updated_at = asset.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                    assets[i] = asset.__dict__

                return {"status": True, "data": assets}, 200


        return {"status": False, "message":"This user don´t have assets yet!"}, 404      


    # ==============================================================================
