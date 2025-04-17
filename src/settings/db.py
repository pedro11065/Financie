import os, json, psycopg2

class Db_connect:

    check: bool

    host:str
    database :str
    user: str
    password : str

    def read_db_info(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'db.json') 

        try:
            with open(file_path, "r") as file:
                config = json.load(file)
            
            self.host = config['db']['host']
            self.database = config['db']['database']
            self.user = config['db']['user']
            self.password = config['db']['password']

            self.check = True
        
        except Exception as error:
            print(f"Erro: {error}")
            self.check = False
        
    def make_connection(self):

        self.read_db_info(self)
        
        if self.check:
            conn = psycopg2.connect(
            host = self.host,
            database = self.database,
            user = self.user,
            password = self.password
            )

            return conn

        else:

            return False
