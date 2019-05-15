import web
import requests

print("Enter a cities name.")
Stad = str(input())

try:
    APIresponse = web.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/') # Hämtar väderprognos.
    Väderprognoser = APIresponse["forecasts"] # Listan forecasts innehåller väderprognoserna som ska användas.
    print("Forecast: ")
    for i in Väderprognoser:
        print(i["date"] + " it is prognosed to be " + i["forecast"]) # Skriver ut väderprognosen för den angivna staden.
except:
    print("Invalid city.") # Om staden inte finns i listan ska meddelandet "Invalid city." skrivas.