import pandas as pd

from business import getFile
from datetime import date
from dateutil.relativedelta import relativedelta
from clase import fileClass as fc
from clase import connClass as cn

from conex import oConn as oConnect

baseURL = 'https://www.gov.br/anac/pt-br/assuntos/regulados/empresas-aereas/Instrucoes-para-a-elaboracao-e-apresentacao-das-demonstracoes-contabeis/envio-de-informacoes/basica/'

listProcessFiles = []
listProcessFiles.append(fc.connClass(
                        urlBase = baseURL
                        ,period = date.today().strftime("%Y-%m")
                        ,year = date.today().strftime("%Y")
                        ,fullPath = baseURL +  date.today().strftime("%Y") +'/basica'+ date.today().strftime("%Y-%m") + '.zip')
)
listProcessFiles.append(fc.connClass(
                        urlBase = baseURL
                        ,period = (date.today() + relativedelta(months=-1)).strftime("%Y-%m")
                        ,year = (date.today() + relativedelta(months=-1)).strftime("%Y")
                        ,fullPath = baseURL + (date.today() + relativedelta(months=-1)).strftime("%Y") +'/basica'+ (date.today() + relativedelta(months=-1)).strftime("%Y-%m") + '.zip')
)

for files in listProcessFiles:
    df = getFile.readFile(files.fullPath, f"basica_{files.period}.zip")
    if df is not None and not df.empty:
        print(files.fullPath)
        break

print(df.head())

# Connect to database snowflake

# auth_data = cn.get_auth_data()

# db = oConnect.AzureSQLDatabase(
#     server=auth_data["server"],
#     database=auth_data["database"],
#     username=auth_data["username"],
#     schema=auth_data["schema"],
#     warehouse=auth_data["warehouse"],
#     role=auth_data["role"],
#     authenticator=auth_data["authenticator"]
# )

# conn = db.connectBD()
# resultados = db.executeQuery("select current_date")
# print(resultados)

# db.connectClose()

