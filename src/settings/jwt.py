import jwt

class auth0:

    def __init__(self):

        key_path: str = r"src\settings\key.key"
        self.key = self.load_key(key_path)

    @staticmethod
    def load_key(file_path) -> bytes:
        with open(file_path, "rb") as file:
            return file.read()
        
    @staticmethod        
    def encrypt(self, data):
        token = jwt.encode(data, self.key, algorithm="HS256")
        return token
    
    @staticmethod
    def decrypt(self, token):
        try:
            decoded_payload = jwt.decode(token, self.key, algorithms=["HS256"])
            return decoded_payload
        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}
        except jwt.InvalidTokenError:
            return {"message": "Invalid token"}

