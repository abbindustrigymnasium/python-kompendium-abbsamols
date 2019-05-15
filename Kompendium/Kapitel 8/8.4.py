import requests
import web
import ui

Artister = web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")["artists"]
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

ui.line()
ui.header("ARTIST DATABASE")
ui.line()
ui.echo("Welcome to a world of music!")
ui.line()
ui.echo ("L | List artists")
ui.echo ("V | View artist profile")
ui.echo ("E | Exit application")
ui.line()
Val = ui.prompt("Selection > ") # Tar emot en input så att programmet kan fortsätta.

while True:
    if Val.lower() == "l":
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        for i in Artister:
            ui.echo(i["name"]) # Om inputen är L skrivs alla namn.
        ui.line(True)
        ui.echo("L | List artists")
        ui.echo("V | View artist profile")
        ui.echo("E | Exit application")
        ui.line()
        Val = ui.prompt("Selection > ") # Tar emot en input så att programmet kan fortsätta.

    if Val.lower() == "v":
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        Artistnamn = ui.prompt("Artist name: ") # Om inputen är V ska man skriva namnet på artisten som man vill få information om.
        for i in Artister:
            if Artistnamn.lower() == i["name"].lower():
                ui.line(True)
                ui.header(i["name"]) # Om namnet finns i listan skrivs det som rubrik.
                ui.line(True)
                url2 = url + str(i["id"]) # Ett nytt url skapas som är unikt för den angivna artisten.
                APIresponse = web.get(url2)
                Members = APIresponse["artist"]["members"]
                Genres = APIresponse["artist"]["genres"]
                Yearsactive = APIresponse["artist"]["years_active"] # Variablen APIresponse tar emot information om den angivna artisten.
                ui.echo("Members:")
                for i in Members:
                    ui.echo(i) # Skriver alla medlemmar.
                ui.echo(" ")
                ui.echo("Genres:")
                for i in Genres:
                    ui.echo(i) # Skriver alla genres.
                ui.echo(" ")
                ui.echo("Years active:")
                for i in Yearsactive:
                    ui.echo(i) # Skriver alla aktiva år.
                ui.line()
                ui.echo("L | List artists")
                ui.echo("V | View artist profile")
                ui.echo("E | Exit application")
                ui.line()
                Val = ui.prompt("Selection > ") # Tar emot en input så att programmet kan fortsätta.

    if Val.lower() == "e":
        ui.echo("Exiting the application.")
        break # Om inputen är E avslutas programmet.

    if Val.lower != "l" or "v" or "e": # Om inputen inte är L, V eller E skriver meddelar programmet att inputen är felaktig och skriver alternativen igen.
        ui.echo("Invalid input.")
        ui.line(True)
        ui.echo("L | List artists")
        ui.echo("V | View artist profile")
        ui.echo("E | Exit application")
        ui.line()
        Val = ui.prompt("Selection > ") # Tar emot en input så att programmet kan fortsätta.