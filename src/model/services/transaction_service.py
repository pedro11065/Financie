from src.model.db.DbController import Db
from src.model.auth.JWT import Auth0
import bcrypt, traceback, uuid, os

from src.model.classes.asset import *
from src.model.classes.liability import *

from datetime import datetime

from src.model.classes.transaction import *

class Transaction_service:

    def __init__(self, payload, request):
        self.db = Db()
        self.payload = payload
        self.request = request.get_json()

        self.user_id : str
        self.liability_id : str
        self.asset_id : str


    # ==============================================================================

    def create(self):

        if self.payload[0]:


            self.user_id = self.payload[1]["id"]
            self.asset_id = self.request["asset_id"]
            self.liability_id = self.request["liability_id"]

            #-----------------------------------------------------------------------


            
            #-----------------------------------------------------------------------

            #O ativo ou passivo vai ser selecionado no front -> id dele

            try:
                # TIPO DE TRANSAÇÃO: SAÍDA (Dinheiro saindo)
                if self.request["transaction_type"] == "payment":


                    # Caso 1: Despesa direta (sem ativo ou passivo envolvido)              
                    if self.liability_id == None and self.asset_id == None and self.request["item"] == False:  # Saldo = Saldo - valor // Transação padrão de pagamento

                        self.db.users.update.balance(self.user_id, self.request["amount"], "deduct")


                    # Caso 2: Pagamento de uma dívida/passivo
                    elif self.liability_id != None and self.asset_id == None: # Saldo = Saldo - valor // Quitação de um passivo ou de uma parcela 
                    # Por enquanto sem sistema de parcelamento
                        
                        self.db.users.update.balance(self.user_id, self.request["amount"], "deduct")
                        self.db.liabilities.delete.liability(self.user_id, self.asset_id,)


                    # Caso 3: Pagamento por um ativo
                    elif self.liability_id == None and self.asset_id == None and self.request["item"] == True: # Saldo = Saldo - valor // Novo ativo
                        
                        asset_obj = Asset(name=self.equest["name"], 
                            description=self.request["description"], 
                            category=self.request["category"],
                            status=self.request["status"],
                            location=self.request["location"], 
                            user_id=self.payload[1]["id"],
                            created_at=datetime.now(),
                            id=uuid.uuid4())
                        
                        self.request["asset_id"] = asset_obj.id
                        self.db.users.update.balance(self.user_id, self.request["amount"], "deduct")
                        self.db.assets.create.asset(asset_obj)
                        

                    # Caso 4: Pagamento de um ativo usando um passivo (ex: cartão de crédito)
                    # ---
                    # elif request["liability_id"] != "" and request["asset_id"] != "":
                        #None


                # TIPO DE TRANSAÇÃO: ENTRADA (Dinheiro entrando)
                elif self.request["transaction_type"] == "receivement":

                    # Caso 1: Renda direta (salário, dividendos, etc.)  
                    if self.asset_id == None and self.liability_id == None: # Saldo = valor + saldo
            
                        self.db.users.update.balance(self.user_id, self.request["amount"], "sum")
                        

                    # Caso 2: Renda de um ativo (aluguel, retorno de investimento, etc.)          
                    elif self.asset_id != None and self.liability_id == None: # Saldo = valor + saldo

                        self.db.users.update.balance(self.user_id, self.request["amount"], "sum") 


                    # Caso 3: Assumindo novo passivo (empréstimo recebido)  
                    elif self.asset_id == None and self.liability_id != None: # Saldo = valor + saldo //Novo passivo

                        liability_obj = Liability(name=self.request["name"], 
                            description=self.request["description"], 
                            category=self.request["category"],
                            status=self.request["status"],
                            location=self.request["location"], 
                            user_id=self.payload[1]["id"],
                            created_at=datetime.now(),
                            id=uuid.uuid4())
                        
                        
                        self.request["liability_id"] = liability_obj.id

                        

                        self.db.users.update.balance(self.user_id, self.request["amount"], "sum")
                        self.db.liability.create.liability(liability_obj)


                    # Caso 4: Ativo vendido com transferência de passivo
                    elif self.asset_id != None and self.liability_id != None: # Saldo = valor + saldo // ativo por passivo
                        None


                # # TIPO DE TRANSAÇÃO: TRANSFERÊNCIA
                # elif request["transaction_type"] == "transfer":
                #     # Caso 1: Transferência entre contas ou ativos
                #     # ---
                #     None


                transaction_obj = Transaction( #Indempendente do tipo de transação, uma transação vai ser criada/registrada

                    id=uuid.uuid4(),

                    user_id=self.payload[1]["id"],

                    asset_id=self.request["asset_id"],
                    liability_id=self.request["liability_id"],

                    credit_card_id=self.request["credit_card_id"], 
                    
                    statement_id=self.request["statement_id"], 

                    transaction_type=self.request["transaction_type"],
                    payment_method=self.request["payment_method"],
                    payment_status=self.request["payment_status"], 
                    currency=self.request["currency"],
                    amount=self.request["amount"],

                    created_at=datetime.now(),
                    updated_at=datetime.now())
            
                if self.db.transactions.create.transaction(transaction_obj):
                    return {"status": True, "message":"Transaction created successfully!"}, 201
                
            except:
                None
            return {"status": False, "message":"Internal server error."}, 500
            
        return {"status": False, "message":self.payload[1]["message"]}, 405 
        

    # ==============================================================================


    def search(self):


        if self.payload[0]:

            user_id = self.payload[1]["id"] ; transaction = False
            type = self.request['type']
        
            if type == "id":


                id = self.request['id']

                if id:
                    
                    transaction = self.db.transactions.search.by_id(user_id, id)

                if transaction:

                    transaction.created_at = transaction.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    transaction.updated_at = transaction.updated_at.strftime('%Y-%m-%d %H:%M:%S')

                    transaction = transaction.__dict__

                    return {"status": True, "data": transaction}, 200
                
                return {"status": False, "message":"transaction not finded."}, 404 
                
         
        #-------------------------------------------------------------------------------

            elif type == "user":

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


            user_id = self.payload[1]["id"] 
            transaction_id = self.request['id']  
            column = self.request['column']
            value = self.request["value"]

            if column in columns:

                if self.db.transactions.update.transaction(user_id, transaction_id, column, value):
                    return {"status": True, "message":"transaction updated successfully!"}, 201
                
                return {"status": False, "message":"Transaction not finded."}, 500
            
            return {"status": False, "message":"Invalid column."}, 405

        return {"status": False, "message":self.payload[1]["message"]}, 405 


    # ==============================================================================

    
    def delete(self):
        
        if self.payload[0]:

            user_id = self.payload[1]["id"] 
            transaction_id = self.request['id'] 

            if self.db.transactions.delete.transaction(user_id, transaction_id):
                return {"status": True, "message":"Transaction deleted successfully!"}, 201
            else:
                return {"status": False, "message":"Transaction not finded."}, 500

        return {"status": False, "message":self.payload[1]["message"]}, 405