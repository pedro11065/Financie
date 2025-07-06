from src.model.db.DbController import Db
from src.model.auth.JWT import Auth0
import bcrypt, traceback, uuid, os

from datetime import datetime

from src.model.classes.transaction import *

class transaction_service:

    def __init__(self, payload, request):
        self.db = Db("transactions")
        self.payload = payload
        self.request = request


    # ==============================================================================

    def create(self):

        if self.payload[0]:

            request = self.request.get_json()

            transaction = Transaction(name=request["name"], 
                description=request["description"], 
                category=request["category"],
                status=request["status"],
                location=request["location"], 
                user_id=self.payload[1]["id"],
                created_at=datetime.now(),
                id=uuid.uuid4())
            
            if self.db.transactions.create.transaction(transaction):
                return {"status": True, "message":"Transaction created successfully!"}, 201
            else:
                return {"status": False, "message":"Internal server error."}, 500
            
        return {"status": False, "message":self.payload[1]["message"]}, 405 
        

    # ==============================================================================


    def search(self):


        if self.payload[0]:

            user_id = self.payload[1]["id"] ; transaction = False
            type = self.request.args.get('type')
        
            if type == "id":


                id = self.request.args.get('id')

                if id:
                    
                    transaction = self.db.transactions.search.by_id(user_id, id)

                if transaction:

                    transaction.created_at = transaction.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    transaction.updated_at = transaction.updated_at.strftime('%Y-%m-%d %H:%M:%S')

                    transaction = transaction.__dict__

                    return {"status": True, "data": transaction}, 200
                
                return {"status": False, "message":"transaction not finded."}, 404 
                
         
        #-------------------------------------------------------------------------------

            if type == "user":

                transactions = self.db.transactions.search.by_user_id(user_id)

                if transactions:

                    for i, transaction in enumerate(transactions):
                        transaction.created_at = transaction.created_at.strftime('%Y-%m-%d %H:%M:%S')
                        transaction.updated_at = transaction.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                        transactions[i] = transaction.__dict__

                    return {"status": True, "data": transactions}, 200


                return {"status": False, "message":"Transaction not finded."}, 404    

            return  {"status": False, "message":"Invalid type."}, 404  
        
        return {"status": False, "message":self.payload[1]["message"]}, 405 
    

    # ==============================================================================


    def update(self):

        if self.payload[0]:

            request = self.request.get_json()

            user_id = self.payload[1]["id"] 
            transaction_id = request['id']  
            column = request['column']
            value = request["value"]

            if column in columns:

                if self.db.transactions.update.transaction(user_id, transaction_id, column, value):
                    return {"status": True, "message":"transaction updated successfully!"}, 201
                
                return {"status": False, "message":"Transaction not finded."}, 500
            
            return {"status": False, "message":"Invalid column."}, 405

        return {"status": False, "message":self.payload[1]["message"]}, 405 


    # ==============================================================================

    
    def delete(self):
        
        if self.payload[0]:

            request = self.request.get_json()

            user_id = self.payload[1]["id"] 
            transaction_id = request['id'] 

            if self.db.transactions.delete.transaction(user_id, transaction_id):
                return {"status": True, "message":"Transaction deleted successfully!"}, 201
            else:
                return {"status": False, "message":"Transaction not finded."}, 500

        return {"status": False, "message":self.payload[1]["message"]}, 405 