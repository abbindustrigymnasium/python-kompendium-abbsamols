import requests

def get (url):
    r = requests.get(url)
    APIresponse = r.json() # Nu innehåller APIresponse objektet vi hämtade från API:et.
    return APIresponse