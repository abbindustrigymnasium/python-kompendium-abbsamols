import requests
url = "http://77.238.56.27/examples/numinfo/?integer=100"
r = requests.get(url)
APIresponse = r.json() # Nu innehåller APIresponse objektet vi hämtade från API:et.
print(response_API)

Heltal = str(input("Ange ett positivt heltal: "))

#API:et fungerar inte.