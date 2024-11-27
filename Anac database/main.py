import pandas as pd

from business import getFile
from datetime import date
from dateutil.relativedelta import relativedelta
from clase import fileClass as fc
from conex import oConn as oConnect


# baseURL = 'https://www.gov.br/anac/pt-br/assuntos/regulados/empresas-aereas/Instrucoes-para-a-elaboracao-e-apresentacao-das-demonstracoes-contabeis/envio-de-informacoes/basica/'

# listProcessFiles = []
# listProcessFiles.append(fc.processFiles(
#                         urlBase = baseURL
#                         ,period = (date.today() + relativedelta(months=-2)).strftime("%Y-%m")
#                         ,year = (date.today() + relativedelta(months=-2)).strftime("%Y")
#                         ,fullPath = baseURL +  (date.today() + relativedelta(months=-2)).strftime("%Y") +'/basica'+ (date.today() + relativedelta(months=-2)).strftime("%Y-%m") + '.zip')
# )
# listProcessFiles.append(fc.processFiles(
#                         urlBase = baseURL
#                         ,period = (date.today() + relativedelta(months=-1)).strftime("%Y-%m")
#                         ,year = (date.today() + relativedelta(months=-1)).strftime("%Y")
#                         ,fullPath = baseURL + (date.today() + relativedelta(months=-1)).strftime("%Y") +'/basica'+ (date.today() + relativedelta(months=-1)).strftime("%Y-%m") + '.zip')
# )


db = oConnect.AzureSQLDatabase(
    server="zd49589.east-us-2.azure",
    database="smartkargo",
    username="bruno.droguett@voeazul.com.br",
    schema = "ad_ods",
    warehouse= "AZULCARGO_WH",
    role="AZULCARGO_USERS",
    authenticator = "externalbrowser"
)

conn = db.connectBD()
resultados = db.executeQuery("select current_date")
print(resultados)
db.connectClose()

# for files in listProcessFiles:
#     if (getFile.fileExists(files.fullPath)) == True:
#         print(files.Period)
#     else:
#         print(files.fullPath)
