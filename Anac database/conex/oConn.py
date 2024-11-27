import pyodbc
from dataclasses import dataclass
from sqlalchemy import create_engine,text
from snowflake.sqlalchemy import URL

@dataclass
class AzureSQLDatabase:
    server: str
    database : str
    username: str
    schema: str
    warehouse: str
    role: str
    authenticator: str
    conn: object = None

    def connectBD(self):
            try:
                self.conn = create_engine(URL(account = self.server,user = self.username,database = self.database,schema = self.schema,warehouse = self.warehouse,role=self.role,authenticator=self.authenticator)).connect()
                print("Conexão estabelecida!")
                return self.conn
            except pyodbc.Error as e:
                print(f"Erro de conexão: {e}")

    def executeQuery(self, query: str):
        try:
            if not self.conn:
                print("Conexão não estabelecida!")
                return None
            resultados = self.conn.execute(text(query)).fetchall()
            return resultados
        except Exception as e:
            print(f"Erro de query: {e}")

    def connectClose(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Conexão fechada!")
