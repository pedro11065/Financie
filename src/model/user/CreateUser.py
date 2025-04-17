import psycopg2, uuid
from colorama import Fore, Style

from settings.db import *

def db_create_user(user : object): # Cria um usuário usando as informações do user_info como parametro, todos os dados são temporários.
    print(Fore.CYAN + '[Banco de dados] ' + Style.RESET_ALL + 'Registrando novo usuário...')
    
    database = Db_connect 
    # Conecta ao banco de dados
    conn = database.make_connection

    # Cria um cursor
    cur = conn.cursor()

    user_id = str(uuid.uuid4()) # Gera um UUID e o converte para string
    
    # Insere os dados principais do usuário para armazenar na tabela
    
    cur.execute(f"INSERT INTO table_users (id, fullname, email, password, birthday, cpf) VALUES ('{user.uuid}', '{user.fullname}', '{user.email}', '{user.password}', '{user.birthday}', '{user.cpf}');")

    # Confirma as mudanças
    conn.commit()

    # Fecha o cursor e encerra a conexão.
    cur.close()
    conn.close()
