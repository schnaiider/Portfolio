from contextlib import contextmanager
import pyodbc
from sqlalchemy import create_engine,text
from snowflake.sqlalchemy import URL
from Project.services import readCFG as cfg

config = cfg.readCFG()


@contextmanager
def dbConnect():
    conn = createConnection()
    try:
        yield conn
    finally:
        closeConnection(conn)

def createConnection():
    try:
        url = URL(account= config['connectInfo']['server'],user= config['connectInfo']['username'],database= config['connectInfo']['database'],schema=config['connectInfo']['schema'],warehouse=config['connectInfo']['warehouse'],role=config['connectInfo']['role'],authenticator=config['connectInfo']['authenticator'])
        engine = create_engine(url, pool_size=10, max_overflow=20)
        return engine.connect()
    except pyodbc.Error as e:
            print(f"Erro de conexão: {e}")
def closeConnection(conn):
    try:
        if conn:
            conn.close()
            print("Conexão fechada!")
    except Exception as e:
        print(f"Erro ao fechar conexão: {e}")

def executeQuery(query: str):
    with dbConnect() as conn:
        resultados = conn.execute(text(query)).fetchall()
        return resultados
    
def blkInsert(tabela: str, dfInsert: any):
    with dbConnect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS ANACBR.{tabela}"))
        dfInsert.to_sql(tabela, conn, schema="ANACBR", if_exists='replace', index=False)
        print("Inserção bem-sucedida!")