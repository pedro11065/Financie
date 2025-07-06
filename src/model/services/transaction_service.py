from src.model.db.DbController import Db
from src.model.auth.JWT import Auth0
import bcrypt, traceback, uuid, os

from datetime import datetime

from src.model.classes.transaction import *

class transaction_service:

    def __init__(self, payload, request):
        self.db = Db()
        self.payload = payload
        self.request = request


    # ==============================================================================

    def create(self):

        if self.payload[0]:

            request = self.request.get_json()

            #-----------------------------------------------------------------------

            transaction = Transaction( #Indempendente do tipo de transação, uma transação vai ser criada/registrada

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

                created_at=datetime.now(),
                updated_at=datetime.now())
            
            #-----------------------------------------------------------------------

            #O ativo ou passivo vai ser selecionado no front -> id dele


            # TIPO DE TRANSAÇÃO: SAÍDA (Dinheiro saindo)
            if request["transaction_type"] == "exit":

                # Caso 1: Despesa direta (sem ativo ou passivo envolvido)
                # Saldo = Saldo - valor // Transação padrão de pagamento
                if request["liability_id"] == "" and request["asset_id"] == "":

                    if self.db.transactions.create.transaction(transaction):
                        return {"status": True, "message":"Transaction created successfully!"}, 201
                    return {"status": False, "message":"Internal server error."}, 500

                # Caso 2: Pagamento de uma dívida/passivo
                # Saldo = Saldo - valor // Quitação de um passivo ou de uma parcela 
                elif request["liability_id"] != "" and request["asset_id"] == "": # Por enquanto sem sistema de parcelamento

                    None

                # Caso 3: Pagamento por um ativo
                # Saldo = Saldo - valor // Novo ativo
                elif request["liability_id"] == "" and request["asset_id"] != "":

                    None

                # Caso 4: Pagamento de um ativo usando um passivo (ex: cartão de crédito)
                # ---
                # elif request["liability_id"] != "" and request["asset_id"] != "":
                    #None

            # TIPO DE TRANSAÇÃO: ENTRADA (Dinheiro entrando)
            elif request["transaction_type"] == "entry":

                # Caso 1: Renda direta (salário, dividendos, etc.)
                # Saldo = valor + saldo
                if request["asset_id"] == "" and request["liability_id"] == "":

                    None

                # Caso 2: Renda de um ativo (aluguel, retorno de investimento, etc.)
                # Saldo = valor + saldo
                elif request["asset_id"] != "" and request["liability_id"] == "":

                    None

                # Caso 3: Assumindo novo passivo (empréstimo recebido)
                # Saldo = valor + saldo //Novo passivo
                elif request["asset_id"] == "" and request["liability_id"] != "":

                    None

                # Caso 4: Ativo vendido com transferência de passivo
                # Saldo = valor + saldo // ativo por passivo
                elif request["asset_id"] != "" and request["liability_id"] != "":

                    None

            # # TIPO DE TRANSAÇÃO: TRANSFERÊNCIA
            # elif request["transaction_type"] == "transfer":
            #     # Caso 1: Transferência entre contas ou ativos
            #     # ---
            #     None


            
            if self.db.transactions.create.transaction(transaction):
                return {"status": True, "message":"Transaction created successfully!"}, 201
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