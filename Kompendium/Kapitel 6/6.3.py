import requests
print("---ARTIST DB---")

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r = requests.get(url)
APIresponse = r.json()
Artister = APIresponse["artists"] # Variabeln "Artister" innehåller alla artister från API:et.

for i in Artister:
    print(i["name"]) # Skriver ut alla artister.

print("-----------------")
print("Select artist: ")
Artist = str(input())

Namn = ["Ariana Grande", "Avicii", "Blink -182", "Brad Paisley", "Ed Sheeran", "Imagine Dragons", "Maroon 5", "Scorpions"]

if Artist.title() in Namn: # Om den angivna artisten finns ska programmet skriva ut artistens namn, genre och medlemmar.
    for i in Artister:
        if i["name"] == Artist.title():
            Artistid = i["id"]
            url = url + str(Artistid)
            r = requests.get(url)
            APIresponse = r.json()

            Genres = APIresponse["artist"]["genres"]
            Members = APIresponse["artist"]["members"]

            print(APIresponse["artist"]["name"])
            print("*****************")
            print("Genres: ")
            for i in Genres:
                print(i)

            print("Years active: " + APIresponse["artist"]["years_active"][0])
            print("Members: ")
            for i in Members:
                print(i)

            print("-----------------")
            break
else:
    print("Invalid input.") # Annars skrivs det att den angivna artisten inte finns i listan.