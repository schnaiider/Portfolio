import pandas as pd
import zipfile
import requests
import tqdm
import os


def fileExists(url,fileName,saveAs):    
    try:
        os.makedirs(os.path.dirname(saveAs+fileName), exist_ok=True)
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()
        fileSize = int(response.headers.get('content-length', 0))
        progressBar = tqdm.tqdm(total=fileSize, unit='B', unit_scale=True)
        with open(saveAs+fileName, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                progressBar.update(len(chunk))
        return saveAs+fileName
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar: {e}")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None
    
def readFileZip(url,fileName,saveAs,_delimiter,_quotechar,_encoding):
    pathZip = fileExists(url,fileName,saveAs)
    if pathZip is None:
        return None
    if not os.path.exists(pathZip):
            print("Arquivo ZIP não encontrado.")
            return None
    if not zipfile.is_zipfile(pathZip):
        print("Arquivo ZIP inválido.")
        return None
    try:
        with zipfile.ZipFile(pathZip, 'r') as zip_ref:
            files = zip_ref.namelist()
            fileProcess = [arq for arq in files if arq.endswith('.txt')]
            if not fileProcess:
                print("Arquivo TXT não encontrado.")
                return None
            with zip_ref.open(fileProcess[0]) as file:
                df = pd.read_csv(file, 
                                delimiter=_delimiter, 
                                quotechar=_quotechar, 
                                encoding=_encoding)
                return df
    except zipfile.BadZipFile as e:
        print(f"Erro ao abrir ZIP: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Erro ao ler arquivo TXT: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    return None