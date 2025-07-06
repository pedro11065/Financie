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

            #-----------------------------------------------------------------------

            # TRANSACTION TYPE: EXIT (Money going out)
            if request["transaction_type"] == "exit":
                if request["liability_id"] == "" and request["asset_id"] == "":
                    # Case 1: Direct expense (no asset or liability involved)
                    None
                elif request["liability_id"] != "" and request["asset_id"] == "":
                    # Case 2: Paying off a liability/debt
                    None
                elif request["liability_id"] == "" and request["asset_id"] != "":
                    # Case 3: Paying for an asset
                    None
                elif request["liability_id"] != "" and request["asset_id"] != "":
                    # Case 4: Paying for an asset using a liability (e.g., credit card)
                    None

            # TRANSACTION TYPE: ENTRY (Money coming in)
            elif request["transaction_type"] == "entry":
                if request["asset_id"] == "" and request["liability_id"] == "":
                    # Case 1: Direct income (salary, dividends, etc.)
                    None
                elif request["asset_id"] != "" and request["liability_id"] == "":
                    # Case 2: Income from an asset (rent, investment return, etc.)
                    None
                elif request["asset_id"] == "" and request["liability_id"] != "":
                    # Case 3: Taking on new liability (loan received)
                    None
                elif request["asset_id"] != "" and request["liability_id"] != "":
                    # Case 4: Asset sold with liability transfer
                    None

            # TRANSACTION TYPE: TRANSFER
            elif request["transaction_type"] == "transfer":
                # Case 1: Transfer between accounts or assets
                None

            transaction = Transaction(

                id=uuid.uuid4(),

                user_id=self.payload[1]["id"],

                asset_id=request["asset_id"],
                liability_id=request["liability_id"],

                credit_card_id=request["credit_card_id"], 
                
                statement_id=request["statement_id"], 

                transaction_type=request["transaction_type"],
                payment_method=request["payment_method"],
                payment_status=request["payment_status"], 
                currency=request["currency"],
                amount=request["amount"],
                created_at=datetime.now()
                )
                
            
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