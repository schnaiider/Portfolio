
import pandas as pd
import zipfile
import io
import requests
import urllib.parse



def fileExists(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        return all([parsed_url.scheme, parsed_url.netloc]) and requests.head(url).status_code < 400
    except requests.RequestException:
        return False