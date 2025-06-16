import jwt as pyjwt
from datetime import date

class Auth0:

    def __init__(self):

        key_path: str = r"src\settings\security\key.key"
        self.key = self.load_key(key_path)

    @staticmethod
    def load_key(file_path) -> bytes:
        with open(file_path, "rb") as file:
            return file.read()
        
    @staticmethod        
    def encrypt(self, payload):
        # Convert date objects to strings
        for key, value in payload.items():
            if isinstance(value, date):
                payload[key] = value.isoformat()
        token = pyjwt.encode(payload, self.key, algorithm="HS256")
        # Ensure compatibility with different return types
        return token if isinstance(token, str) else token.decode('utf-8')
        
    @staticmethod
    def decrypt(self, token):
        try:
            decoded_payload = pyjwt.decode(token, self.key, algorithms=["HS256"])
            return decoded_payload
        except pyjwt.ExpiredSignatureError:
            return {"message": "Token has expired"}
        except pyjwt.InvalidTokenError:
            return {"message": "Invalid token"}

