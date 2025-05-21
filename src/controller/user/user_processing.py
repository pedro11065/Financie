from src.model.db import Db
from src.settings.jwt import auth0
import bcrypt,os

from src.model.user.user import User

class User_api_process:

    def __init__(self):
        self.db = Db("users")

    def login(self,data):

        try:


            user = self.db.users.search.by_email(data["email"])
            
            if not user:
                return {"Status": False, "message":"User don´t exist."}, 404

            if not bcrypt.checkpw(data["password"].encode(), user.password.encode()):
                return {"status": False, "message":"Wrong password."}, 401  


            payload = {"id" : user.id, 
                    "email": user.email, 
                    "fullname": user.fullname, 
                    "phone": user.phone, 
                    "birthday": user.birthday}


            auth = auth0()
            token = auth.encrypt(auth, payload)
            
            return {
                "status": True,
                "token": token,
                "message":"Login successfully."
            }, 200

        except Exception as e:
            print(e)
            return {"message": "Internal server error"}, 500

    def register(self, data):

        user = User(fullname=data["fullname"], 
            cpf=data["cpf"], 
            email=data["email"],
            phone=data["phone"],
            password=data["password"], 
            birthday=data["birthday"])
        
        if self.db.users.create.user(user):
            return {"status": True, "message":"User created successfully!"}, 201
        else:
            return {"status": False, "message":"Internal server error."}, 500
        
    def forget_password( self,data):
            
            user = self.db.users.search.by_cpf(data["cpf"])
    
            if user:

                email = user.email
                #criar envio de email para a troca de senha
                
            
            