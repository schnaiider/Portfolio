
import pandas as pd
import zipfile
import requests
import tqdm
import os



def fileExists(url,fileName):
    
    caminho_salvar = "schnaiide/Downloads/"+fileName

    try:
        # Criar diretório se não existir
        os.makedirs(os.path.dirname(caminho_salvar), exist_ok=True)

        # Baixar arquivo
        resposta = requests.get(url, stream=True, timeout=60)
        resposta.raise_for_status()

        tamanho_arquivo = int(resposta.headers.get('content-length', 0))
        barra_progresso = tqdm.tqdm(total=tamanho_arquivo, unit='B', unit_scale=True)

        with open(caminho_salvar, "wb") as arquivo:
            for chunk in resposta.iter_content(chunk_size=1024):
                arquivo.write(chunk)
                barra_progresso.update(len(chunk))

        print(f"Download concluído em {caminho_salvar}")
        return caminho_salvar
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar: {e}")
        return None
    except Exception as e:
        print(f"Erro: {e}")
        return None
    
    
def readFile(url,fileName):
    caminho_zip = fileExists(url,fileName)
    if caminho_zip is None:
        return None

    if not os.path.exists(caminho_zip):
            print("Arquivo ZIP não encontrado.")
            return None
        
    if not zipfile.is_zipfile(caminho_zip):
        print("Arquivo ZIP inválido.")
        return None

    try:
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            arquivos = zip_ref.namelist()
            print(f"Arquivos encontrados: {arquivos}")
            
            arquivo_txt = [arq for arq in arquivos if arq.endswith('.txt')]
            if not arquivo_txt:
                print("Arquivo TXT não encontrado.")
                return None
            
            with zip_ref.open(arquivo_txt[0]) as file:
                df = pd.read_csv(file, 
                                delimiter=';', 
                                quotechar='"', 
                                encoding='latin1')
                return df
    
    except zipfile.BadZipFile as e:
        print(f"Erro ao abrir ZIP: {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Erro ao ler arquivo TXT: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    
    
    
    return None