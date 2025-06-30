from src.model.db.DbController import Db
from src.model.settings.security.auth0 import Auth0
import bcrypt, traceback, uuid, os

from datetime import datetime

from src.model.classes.liability import *

class Liability_service:

    def __init__(self, payload, request):
        self.db = Db("liabilities")
        self.payload = payload
        self.request = request


    # ==============================================================================

    def create(self):

        if self.payload[0]:

            request = self.request.get_json()

            liability = Liability(name=request["name"], 
                description=request["description"], 
                category=request["category"],
                status=request["status"],
                location=request["location"], 
                user_id=self.payload[1]["id"],
                created_at=datetime.now(),
                id=uuid.uuid4())
            
            if self.db.liabilities.create.liability(liability):
                return {"status": True, "message":"Liability created successfully!"}, 201
            else:
                return {"status": False, "message":"Internal server error."}, 500
            
        return {"status": False, "message":self.payload[1]["message"]}, 405 
        

    # ==============================================================================


    def search(self):


        if self.payload[0]:

            user_id = self.payload[1]["id"] 
            id = self.request.args.get('id') ;  type = self.request.args.get('type')
        
            if type == "id":

                liability = self.db.liabilities.search.by_id(user_id, id)

                if liability:

                    liability.created_at = liability.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    liability.updated_at = liability.updated_at.strftime('%Y-%m-%d %H:%M:%S')

                    liability = liability.__dict__

                    return {"status": True, "data": liability}, 200
                
                return {"status": False, "message":"Asset not finded."}, 404 
                
         
        #-------------------------------------------------------------------------------

            if type == "user":

                assets = self.db.assets.search.by_user_id(id)

                if assets:

                    for i, liability in enumerate(assets):
                        liability.created_at = liability.created_at.strftime('%Y-%m-%d %H:%M:%S')
                        liability.updated_at = liability.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                        assets[i] = liability.__dict__

                    return {"status": True, "data": assets}, 200


                return {"status": False, "message":"Asset not finded."}, 404    

            return  {"status": False, "message":"Invalid type."}, 404  
        
        return {"status": False, "message":self.payload[1]["message"]}, 405 
    

    # ==============================================================================


    def update(self):

        if self.payload[0]:

            request = self.request.get_json()

            user_id = self.payload[1]["id"] 
            asset_id = request['id']  
            column = request['column']
            value = request["value"]

            if self.db.assets.update.asset(user_id, asset_id, column, value):
                return {"status": True, "message":"Asset updated successfully!"}, 201
            else:
                return {"status": False, "message":"Asset not finded."}, 500
            
        return {"status": False, "message":self.payload[1]["message"]}, 405 


    # ==============================================================================

    
    def delete(self):
        
        if self.payload[0]:

            request = self.request.get_json()

            user_id = self.payload[1]["id"] 
            asset_id = request['id'] 

            if self.db.assets.delete.asset(user_id, asset_id):
                return {"status": True, "message":"Asset deleted successfully!"}, 201
            else:
                return {"status": False, "message":"Asset not finded."}, 500

        return {"status": False, "message":self.payload[1]["message"]}, 405 