from cryptography.fernet import Fernet

class Crypt:
    def __init__(self, key_path: str = "src/settings/key.key"):
        self.key = self.load_key(key_path)
        self.fernet = Fernet(self.key)

    @staticmethod
    def load_key(file_path: str) -> bytes:
        with open(file_path, "rb") as file:
            return file.read()

    def encrypt(self, data: str) -> bytes:

        if isinstance(data, str):
            return self.fernet.encrypt(data.encode())
        
        elif isinstance(data, bytes):
            return self.fernet.encrypt(data)
        return data

    def decrypt(self, encrypted_data) -> str:
        
        if isinstance(encrypted_data, bytes):
            return self.fernet.decrypt(encrypted_data).decode()
        return encrypted_data