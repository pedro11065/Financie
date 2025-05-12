from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("chave.key", "wb") as archive:
        archive.write(key)

    return key

def load_key():
    with open("chave.key", "rb") as archive:
        return archive.read()

def encrypt(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()


key = b'r0NYuWCZpry4LqNTyUelgQXBZRJZEZ35dU7aqJxomig='
print(f"Generated Key: {key}")

cpf = "50774811803"
encrypted_cpf = b'gAAAAABoIS4mear8fpDo5llEaoNu6nVbyR3qtFUmqFjY2fzBzETbQw9UrMYvcLQjz5ePiLCsZCDiPnTJuLU0omgOSgWpByDWPw=='
print(f"Encrypted CPF: {encrypted_cpf}")

decrypted_cpf = decrypt(encrypted_cpf, key)
print(f"Decrypted CPF: {decrypted_cpf}")