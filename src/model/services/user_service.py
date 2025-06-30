from src.model.db.DbController import Db
from src.model.settings.security.auth0 import Auth0
import bcrypt, traceback

from src.model.classes.user import User

class User_service:

    def __init__(self, payload, request):
        self.db = Db("users")
        self.payload = payload
        self.request = request

    def login(self):

        request = self.request.get_json()
        
        try:

            user = self.db.users.search.by_email(request["email"])
            
            if not user:
                return {"Status": False, "message":"User don´t exist."}, 404

            if not bcrypt.checkpw(request["password"].encode(), user.password.encode()):
                return {"status": False, "message":"Wrong password."}, 401  


            payload = {"id" : user.id, 
                    "email": user.email, 
                    "fullname": user.fullname, 
                    "phone": user.phone, 
                    "birthday": user.birthday}


            auth = Auth0()
            token = auth.encrypt(payload)
            
            return {
                "status": True,
                "token": token,
                "message":"Login successfully."
            }, 200

        except Exception as e:
            print(e)
            tb = traceback.extract_tb(e.__traceback__)
            file_name, line_number, _, _ = tb[-1]
            
            print(f"Error in {file_name} at line {line_number}")
            
            return {"message": "Internal server error"}, 500

#------------------------------------------------------------------------

    def register(self):

        request = self.request.get_json()
            
        user = User(fullname=request["fullname"], 
            cpf=request["cpf"], 
            email=request["email"],
            phone=request["phone"],
            password=request["password"], 
            birthday=request["birthday"])
        
        if self.db.users.create.user(user):
            return {"status": True, "message":"User created successfully!"}, 201
        else:
            return {"status": False, "message":"Internal server error."}, 500
        
    def forget_password( self,data):
            
            user = self.db.users.search.by_cpf(data["cpf"])
    
            if user:

                email = user.email
                #criar envio de email para a troca de senha
                
            
            