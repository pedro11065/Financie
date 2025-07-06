from src.model.db.DbController import Db
from src.model.auth.JWT import Auth0
import bcrypt, traceback, uuid, os

from datetime import datetime

from src.model.classes.liability import *

class Liability_service:

    def __init__(self, payload, request):
        self.db = Db()
        self.payload = payload
        self.request = request


    # ==============================================================================

    def create(self):

        if self.payload[0]:

            request = self.request.get_json()

            liability = Transaction(name=request["name"], 
                description=request["description"], 
                category=request["category"],
                status=request["status"],
                location=request["location"], 
                user_id=self.payload[1]["id"],
                created_at=datetime.now(),
                id=uuid.uuid4())
            
            if self.db.transactions.create.liability(liability):
                return {"status": True, "message":"Liability created successfully!"}, 201
            else:
                return {"status": False, "message":"Internal server error."}, 500
            
        return {"status": False, "message":self.payload[1]["message"]}, 405 
        

    # ==============================================================================


    def search(self):


        if self.payload[0]:

            request = self.request.get_json()

            user_id = self.payload[1]["id"] ; liability = False
            type = request['type']
        
            if type == "id":

                id = request['id'] 

                if id:
                    
                    liability = self.db.transactions.search.by_id(user_id, id)

                if liability:

                    liability.created_at = liability.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    liability.updated_at = liability.updated_at.strftime('%Y-%m-%d %H:%M:%S')

                    liability = liability.__dict__

                    return {"status": True, "data": liability}, 200
                
                return {"status": False, "message":"liability not finded."}, 404 
                
         
        #-------------------------------------------------------------------------------

            if type == "user":

                liabilities = self.db.transactions.search.by_user_id(user_id)

                if liabilities:

                    for i, liability in enumerate(liabilities):
                        liability.created_at = liability.created_at.strftime('%Y-%m-%d %H:%M:%S')
                        liability.updated_at = liability.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                        liabilities[i] = liability.__dict__

                    return {"status": True, "data": liabilities}, 200


                return {"status": False, "message":"Liability not finded."}, 404    

            return  {"status": False, "message":"Invalid type."}, 404  
        
        return {"status": False, "message":self.payload[1]["message"]}, 405 
    

    # ==============================================================================


    def update(self):

        if self.payload[0]:

            request = self.request.get_json()

            user_id = self.payload[1]["id"] 
            liability_id = request['id']  
            column = request['column']
            value = request["value"]

            if column in columns:

                if self.db.transactions.update.liability(user_id, liability_id, column, value):
                    return {"status": True, "message":"liability updated successfully!"}, 201
                
                return {"status": False, "message":"Liability not finded."}, 500
            
            return {"status": False, "message":"Invalid column."}, 405

        return {"status": False, "message":self.payload[1]["message"]}, 405 


    # ==============================================================================

    
    def delete(self):
        
        if self.payload[0]:

            request = self.request.get_json()

            user_id = self.payload[1]["id"] 
            liability_id = request['id'] 

            if self.db.transactions.delete.liability(user_id, liability_id):
                return {"status": True, "message":"Liability deleted successfully!"}, 201
            else:
                return {"status": False, "message":"Liability not finded."}, 500

        return {"status": False, "message":self.payload[1]["message"]}, 405 