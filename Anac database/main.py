import pandas as pd

from business import getFile
from datetime import date
from dateutil.relativedelta import relativedelta
from clase import fileClass as fc
from clase import connClass as cn
from clase import companyClass as compObj

from conex import oConn as oConnect
import snowflake.connector as snConn


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

dfCompanyGroup = df.groupby(['id_empresa', 'sg_empresa_icao', 'sg_empresa_iata', 'nm_empresa', 'nm_pais', 'ds_tipo_empresa']).size().reset_index()
companys = [compObj.company(*row[1:]) for row in dfCompanyGroup.itertuples(index=False)]
dfCompany = pd.DataFrame([c.__dict__ for c in companys])

auth_data = cn.get_auth_data()

db = oConnect.AzureSQLDatabase(
    server=auth_data["server"],
    database=auth_data["database"],
    username=auth_data["username"],
    schema=auth_data["schema"],
    warehouse=auth_data["warehouse"],
    role=auth_data["role"],
    authenticator=auth_data["authenticator"]
)

conn = db.connectBD()


db.blkInsert(
    tabela = "RAWCOMPANY"
    ,dfInsert=dfCompany
    )

db.connectClose()
