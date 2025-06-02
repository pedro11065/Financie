from src.model.db import Db
from src.settings.security.auth0 import Auth0
import bcrypt, traceback, uuid

from datetime import datetime

from src.model.asset.asset import *

class Asset_api_process:

    def __init__(self):
        self.db = Db("assets")

    def create(self, data):

        asset = Asset(name=data["name"], 
            description=data["description"], 
            category=data["category"],
            status=data["status"],
            location=data["location"], 
            user_id=["user_id"],
            created_at=datetime.now(),
            id=uuid.uuid4())
        
        if self.db.assets.create.asset(asset):
            return {"status": True, "message":"Asset created successfully!"}, 201
        else:
            return {"status": False, "message":"Internal server error."}, 500
        
                
            
            