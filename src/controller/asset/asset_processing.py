from src.model.db import Db
from src.settings.security.auth0 import Auth0
import bcrypt, traceback, uuid, os

from datetime import datetime

from src.model.asset.asset import *

class Asset_api_process:

    def __init__(self):
        self.db = Db("assets")


    # ==============================================================================

    def create(self, payload, request):

        if payload[0]:

            data = request.get_json()

            asset = Asset(name=data["name"], 
                description=data["description"], 
                category=data["category"],
                status=data["status"],
                location=data["location"], 
                user_id=payload[1]["id"],
                created_at=datetime.now(),
                id=uuid.uuid4())
            
            if self.db.assets.create.asset(asset):
                return {"status": True, "message":"Asset created successfully!"}, 201
            else:
                return {"status": False, "message":"Internal server error."}, 500
            
        return {"status": False, "message":payload[1]["message"]}, 405 
        
    
     # ==============================================================================


    def search(self, payload, request):


        if payload[0]:

            user_id = payload[1]["id"] 
            id = request.args.get('id') ;  type = request.args.get('type')
        
            if type == "id":

                asset = self.db.assets.search.by_id(user_id, id)

                if asset:

                    asset.created_at = asset.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    asset.updated_at = asset.updated_at.strftime('%Y-%m-%d %H:%M:%S')

                    asset = asset.__dict__

                    return {"status": True, "data": asset}, 200
                
                return {"status": False, "message":"Asset not finded."}, 404 
                
         
        #-------------------------------------------------------------------------------

            if type == "user":

                assets = self.db.assets.search.by_user_id(id)

                if assets:

                    for i, asset in enumerate(assets):
                        asset.created_at = asset.created_at.strftime('%Y-%m-%d %H:%M:%S')
                        asset.updated_at = asset.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                        assets[i] = asset.__dict__

                    return {"status": True, "data": assets}, 200


                return {"status": False, "message":"Asset not finded."}, 404    

            return  {"status": False, "message":"Invalid type."}, 404  
        
        return {"status": False, "message":payload[1]["message"]}, 405 


    # ==============================================================================
