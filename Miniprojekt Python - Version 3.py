import random

Antal_poäng = 0
Antal_frågor = 0

print("Välkommen till en frågesport där du har nytta av att vara allmänbildad! Svara 1, X eller 2 på frågorna.")
print("Lycka till!")

Frågor = [{"Fråga": "Vem var Michael Jacksons första fru?", "Alt1": "Lisa Marie Presley", "Alt2": "Priscilla Presley", "Alt3": "Debbie Rowe", "Rätt_svar": "Lisa Marie Presley"},
{"Fråga": "I vilket av följande länder finns floden Donau?", "Alt1": "Bosnien-Hercegovina", "Alt2": "Kroatien", "Alt3": "Slovenien", "Rätt_svar": "Kroatien"},
{"Fråga": "Vad hette uppdraget som förde upp de första människorna till månen?", "Alt1": "Apollo 11", "Alt2": "Apollo 12", "Alt3": "Apollo 13", "Rätt_svar": "Apollo 11"},
{"Fråga": "År 1892 byggdes Sveriges första velodrom, i vilken stad?", "Alt1": "Malmö", "Alt2": "Helsingborg", "Alt3": "Lund", "Rätt_svar": "Lund"},
{"Fråga": "Vilket av följande bilmärken är inte tyskt?", "Alt1": "Porsche", "Alt2": "Fiat", "Alt3": "BMW", "Rätt_svar": "Fiat"}] # Dictionary med frågor, alternativ och rätt svar.
random.shuffle(Frågor) # Frånornas ordning slumpas.

for Fråga in Frågor: # for-loopen görs för varje fråga i dictionaryn Frågor.
    print("")
    print("Fråga " + str(Antal_frågor + 1) + ": " + Fråga["Fråga"]) # Frågan skrivs.
    print("Alternativ:")
    Alternativ = [Fråga["Alt1"], Fråga["Alt2"], Fråga["Alt3"]] # Gör en lista med alternativen.
    random.shuffle(Alternativ) # Alternativens ordning slumpas.
    print("1: " + Alternativ[0]) # Alternativen skrivs.
    print("X: " + Alternativ[1])
    print("2: " + Alternativ[2])

    Svar = str(input("Ange ditt svar: ")) # Tar emot svaret som en string.

    if Svar == "1":
        if Fråga["Rätt_svar"] == Alternativ[0]:
            print("Rätt!")
            Antal_poäng += 1
        else:
            if Fråga["Rätt_svar"] == Alternativ[1]:
                print("Fel, rätt svar är X, " + Alternativ[1] + ".")
            else:
                print("Fel, rätt svar är 2, " + Alternativ[2] + ".")

    elif Svar.lower() == "x":
        if Fråga["Rätt_svar"] == Alternativ[1]:
            print("Rätt!")
            Antal_poäng += 1
        else:
            if Fråga["Rätt_svar"] == Alternativ[0]:
             print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
        
    elif Svar == "2":
        if Fråga["Rätt_svar"] == Alternativ[2]:
            print("Rätt!")
            Antal_poäng += 1
        else:
            if Fråga["Rätt_svar"] == Alternativ[0]:
                print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är X, " + Alternativ[1] + ".")

    elif Svar != "1" and Svar.lower != "x" and Svar != "2":
        if Fråga["Rätt_svar"] == Alternativ[0]:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        elif Fråga["Rätt_svar"] == Alternativ[1]:
            print("Fel, rätt svar är X, " + Alternativ[1] + ".")
        elif Fråga["Rätt_svar"] == Alternativ[2]:
            print("Fel, rätt svar är 2, " + Alternativ[2] + ".")
        print("Kom ihåg att svara 1, X eller 2.")

    
    Antal_frågor += 1

    if Antal_frågor < 5:
        print("Du har just nu " + str(Antal_poäng) + " poäng.")
    else:
        print("")
        print("Frågesporten är slut. Du fick " + str(Antal_poäng) + " av " + str(Antal_frågor) + " poäng.") # Skriver hur många poäng man fick.