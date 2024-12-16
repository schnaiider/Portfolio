import pandas as pd

from util import readCFG 
from modelos import file, airport, company, identifierDigit ,lineType ,plane
from util import readFile

from dateutil.relativedelta import relativedelta
from datetime import date

config = readCFG.readCFG()
listProcessFiles = []

listProcessFiles.append(file.file(
                        urlBase = config["pathBasicAnac"]["url"]
                        ,period = date.today().strftime("%Y-%m")
                        ,year = date.today().strftime("%Y")
                        ,fullPath = config["pathBasicAnac"]["url"] +  date.today().strftime("%Y") +'/basica'+ date.today().strftime("%Y-%m") + '.zip')
)
listProcessFiles.append(file.file(
                        urlBase = config["pathBasicAnac"]["url"]
                        ,period = (date.today() + relativedelta(months=-1)).strftime("%Y-%m")
                        ,year = (date.today() + relativedelta(months=-1)).strftime("%Y")
                        ,fullPath = config["pathBasicAnac"]["url"] + (date.today() + relativedelta(months=-1)).strftime("%Y") +'/basica'+ (date.today() + relativedelta(months=-1)).strftime("%Y-%m") + '.zip')
)
listProcessFiles.append(file.file(
                        urlBase = config["pathBasicAnac"]["url"]
                        ,period = (date.today() + relativedelta(months=-2)).strftime("%Y-%m")
                        ,year = (date.today() + relativedelta(months=-2)).strftime("%Y")
                        ,fullPath = config["pathBasicAnac"]["url"] + (date.today() + relativedelta(months=-2)).strftime("%Y") +'/basica'+ (date.today() + relativedelta(months=-2)).strftime("%Y-%m") + '.zip')
)

for files in listProcessFiles:
    df = readFile.readFileZip(files.fullPath,f"basica_{files.period}.zip",r"C:\\Users\\xuzik\\Desktop\\Anac ETL\\Anac-ETL\\docs\\",';','"','latin1')
    if df is not None and not df.empty:
        print(files.fullPath)
        break

dfCompanyGroup = df.groupby(['id_empresa', 'sg_empresa_icao', 'sg_empresa_iata', 'nm_empresa', 'nm_pais', 'ds_tipo_empresa']).size().reset_index()
companys = [company.company(*row[1:]) for row in dfCompanyGroup.itertuples(index=False)]
dfCompany = pd.DataFrame([c.__dict__ for c in companys])

print(dfCompany)