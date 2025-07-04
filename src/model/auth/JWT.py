import jwt as pyjwt
from datetime import date

import os

class Auth0:

    def __init__(self):

        main_path = os.getcwd()

        key_path: str = r"src\model\settings\auth\key.key"
        self.key = self.load_key(key_path)

    @staticmethod
    def load_key(file_path) -> bytes:
        with open(file_path, "rb") as file:
            return file.read()
        
              
    def encrypt(self, payload):

        if payload:

            for key, value in payload.items():
                if isinstance(value, date):
                    payload[key] = value.isoformat()
            token = pyjwt.encode(payload, self.key, algorithm="HS256")

            return token if isinstance(token, str) else token.decode('utf-8')
    
    
    def decrypt(self, token):

        if token: #Se o token não for None

            try:

                token = token.replace('Bearer ', '')

                decoded_payload = pyjwt.decode(token, self.key, algorithms=["HS256"]) #Decodificando
                return True, decoded_payload
            
            except pyjwt.ExpiredSignatureError:
                return False, {"message": "Token has expired"}
            
            except pyjwt.InvalidTokenError:
                None

            return False, {"message": "Invalid token"}
        
        return False, {"message": "No Token"}

