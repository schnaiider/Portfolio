
from contextlib import contextmanager
import pyodbc
from sqlalchemy import create_engine,text
from snowflake.sqlalchemy import URL
from Project.services import readCFG as cfg

config = cfg.readCFG()
_conn = None

@contextmanager
def dbConnect():
    global _conn
    if _conn is None:
        _conn = createConnection()
    try:
        yield _conn
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        pass

def createConnection():
    try:
        url = URL(account= config['connectInfo']['server'],user= config['connectInfo']['username'],database= config['connectInfo']['database'],schema=config['connectInfo']['schema'],warehouse=config['connectInfo']['warehouse'],role=config['connectInfo']['role'],authenticator=config['connectInfo']['authenticator'])
        engine = create_engine(url, pool_size=10, max_overflow=20)
        return engine.connect()
    except pyodbc.Error as e:
            print(f"Erro de conexão: {e}")
def closeConnection():
    global _conn
    try:
        if _conn:
            _conn.close()
            _conn = None
            print("Conexão fechada!")
    except Exception as e:
        print(f"Erro ao fechar conexão: {e}")

def executeQuery(query: str):
    with dbConnect() as conn:
        resultados = conn.execute(text(query)).fetchall()
        return resultados
    
def blkInsert(tabela: str, dfInsert: any):
    try:
        with dbConnect() as conn:
            tabela_formatada = f'{tabela.replace("'",'').upper()}'
            conn.execute(text(f"DROP TABLE IF EXISTS ANACBR.{tabela}"))
            dfInsert.to_sql(tabela_formatada, conn, schema="ANACBR", if_exists='replace', index=False)
            conn.commit()
            print("Inserção bem-sucedida!")
    except Exception as e:
        print(f"Erro: {e}")