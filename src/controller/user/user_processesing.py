from src.model.db import Db
from src.settings.jwt import auth0
import bcrypt,os

class User_api_process:

    @staticmethod
    def login(data):

        try:

            table = "users"
            db = Db(table)

            user = db.users.search.by_email(data["email"])
            
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

    @staticmethod
    def register(data):
        None