import requests

Städer = [
    "Stockholm",
    "Göteborg",
    "Malmö",
    "Uppsala",
    "Västerås"
]

Stad = str(input("Ange en stad: ")) # Den angivna staden blir en variabel.


if Stad in Städer:
    url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/" + Stad # URL:en för vädret i den angivna staden
    r = requests.get(url)
    response_API = r.json() # Nu innehåller response_API objektet vi hämtade från API:et.
    forecasts = response_API["forecasts"]
    print("Väderprognosen i " + Stad + ":")
    print("**********************")
    print(forecasts[0]["date"] + " the weather will be " + forecasts[0]["forecast"] + ".") # Skriver ut väderprognosen för den angivna staden.
    print(forecasts[1]["date"] + " the weather will be " + forecasts[1]["forecast"] + ".")
    print(forecasts[2]["date"] + " the weather will be " + forecasts[2]["forecast"] + ".")
    print(forecasts[3]["date"] + " the weather will be " + forecasts[3]["forecast"] + ".")
    print(forecasts[4]["date"] + " the weather will be " + forecasts[4]["forecast"] + ".")

else:
    print("**********************")
    print("Det finns ingen väderprognos för den angivna staden.")