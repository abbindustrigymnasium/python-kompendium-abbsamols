Antal_poäng = 0
Antal_frågor = 0

print("Välkommen till en frågesport där du har nytta av att vara allmänbildad! Svara 1, X eller 2 på frågorna.")
print("Lycka till!")

Frågor = [{"Fråga": "Vem var Michael Jacksons första fru?", "Alt1": "Lisa Marie Presley", "Alt2": "Priscilla Presley", "Alt3": "Debbie Rowe", "Rätt_svar": 1},
{"Fråga": "I vilket av följande länder finns floden Donau?", "Alt1": "Bosnien-Hercegovina", "Alt2": "Kroatien", "Alt3": "Slovenien", "Rätt_svar": "X"},
{"Fråga": "Vad hette uppdraget som förde upp de första människorna till månen?", "Alt1": "Apollo 11", "Alt2": "Apollo 12", "Alt3": "Apollo 13", "Rätt_svar": 1},
{"Fråga": "År 1892 byggdes Sveriges första velodrom, i vilken stad?", "Alt1": "Malmö", "Alt2": "Helsingborg", "Alt3": "Lund", "Rätt_svar": 2},
{"Fråga": "Vilket av följande bilmärken är inte tyskt?", "Alt1": "Porsche", "Alt2": "Fiat", "Alt3": "BMW", "Rätt_svar": "X"}] # Dictionary med frågor, alternativ och rätt svar.

for Fråga in Frågor: # Programmet görs för alla frågor.
    print("")
    print("Fråga " + str(Antal_frågor + 1) + ": " + Fråga["Fråga"]) # Frågan skrivs.
    print("Alternativ:") # Alternativen skrivs.
    print("1: " + Fråga["Alt1"])
    print("X: " + Fråga["Alt2"])
    print("2: " + Fråga["Alt3"])

    Svar = str(input("Ange ditt svar: ")) # Tar emot svaret som en string.

    if Svar == "1":
        if Fråga["Rätt_svar"] == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Fråga["Rätt_svar"] == "X":
            print("Fel, rätt svar är X, " + Fråga["Alt2"] + ".")
        elif Fråga["Rätt_svar"] == 2:
            print("Fel, rätt svar är 2, " + Fråga["Alt3"] + ".")

    elif Svar.lower() == "x":
        if Fråga["Rätt_svar"] == 1:
            print("Fel, rätt svar är 1, " + Fråga["Alt1"] + ".")
        elif Fråga["Rätt_svar"] == "X":
            print("Rätt!")
            Antal_poäng += 1
        elif Fråga["Rätt_svar"] == 2:
            print("Fel, rätt svar är 2, " + Fråga["Alt3"] + ".")
        
    elif Svar == "2":
        if Fråga["Rätt_svar"] == 1:
            print("Fel, rätt svar är 1, " + Fråga["Alt1"] + ".")
        elif Fråga["Rätt_svar"] == "X":
            print("Fel, rätt svar är X, " + Fråga["Alt2"] + ".")
        elif Fråga["Rätt_svar"] == 2:
            print("Rätt!")
            Antal_poäng += 1

    elif Svar != "1" and Svar.lower != "x" and Svar != "2":
        if Fråga["Rätt_svar"] == 1:
            print("1")
            print("Fel, rätt svar är 1, " + Fråga["Alt1"] + ".")
        elif Fråga["Rätt_svar"] == "X":
            print("X")
            print("Fel, rätt svar är X, " + Fråga["Alt2"] + ".")
        elif Fråga["Rätt_svar"] == 2:
            print("2")
            print("Fel, rätt svar är 2, " + Fråga["Alt3"] + ".")
        print("Kom ihåg att svara 1, X eller 2.")

    
    Antal_frågor += 1

    if Antal_frågor < 5:
        print("Du har just nu " + str(Antal_poäng) + " poäng.")
    else:
        print("")
        print("Frågesporten är slut. Du fick " + str(Antal_poäng) + " av " + str(Antal_frågor) + " poäng.") # Skriver hur många poäng man fick.