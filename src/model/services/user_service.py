from src.model.db.DbController import Db
import bcrypt, traceback
from src.model.auth.JWT import *
from src.model.classes.user import User

from datetime import datetime

class User_service:

    def __init__(self, payload, request):
        self.db = Db()
        self.payload = payload
        self.request = request

    def login(self):

        request = self.request.get_json()
        
        try:

            query = self.db.users.search.by_email(request["email"])
            
            if query[0]:
                
                if not bcrypt.checkpw(request["password"].encode(), query[0].password_hash.encode()):
                    return {"status": False, "message":"Wrong password."}, 401  


                payload = {"id" : query[0].id, 
                        "email": query[0].email, 
                        "fullname": query[0].fullname, 
                        "phone": query[0].phone, 
                        "birthday": query[0].birthday,
                        "creation": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}


                auth = Auth0()
                token = auth.encrypt(payload)
                
                return {
                    "status": True,
                    "token": token,
                    "message":"Login successfully."
                }, 200
            
            return {"Status": False, "message": query[1]}, 404

        except Exception as e:
            print(traceback.format_exc())
            return {"message": "Internal server error"}, 500

#------------------------------------------------------------------------

    def register(self):

        request = self.request.get_json()
            
        user = User(fullname=request["fullname"], 
            cpf=request["cpf"], 
            email=request["email"],
            phone=request["phone"],
            password_hash=request["password"], 
            birthday=request["birthday"],)
        
        request = self.db.users.create.user(user)

        if request[0]:
            return {"status": True, "message": request[1]}, 201
        else:
            return {"status": False, "message": request[1]}, 500

#------------------------------------------------------------------------
        
    def forget_password( self,data):
            
            user = self.db.users.search.by_cpf(data["cpf"])
    
            if user:

                email = user.email
                #criar envio de email para a troca de senha
                
            
            