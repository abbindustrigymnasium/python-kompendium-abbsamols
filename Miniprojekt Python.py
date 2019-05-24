import random

Antal_poäng = 0
Antal_frågor = 0

print("Välkommen till en frågesport där du har nytta av att vara allmänbildad! Svara 1, X eller 2 på frågorna.")
print("Lycka till!")

Frågor = [1, 2, 3, 4, 5]
while Antal_frågor < 4: # Bestämmer slumpvis vilken fråga som ska ställas. Om antal ställda frågor är mindre än 4 körs while-loopen igen.
    Frågenr = random.randint(1, 5)
    while Frågenr not in Frågor:
        Frågenr = random.randint(1, 5)
    Frågor.remove(Frågenr)


    if Frågenr == 1:
        print("")
        print("Fråga " + str(Antal_frågor + 1) + ": Vem var Michael Jacksons första fru?")
        Alternativ = ["Lisa Marie Presley", "Priscilla Presley", "Debbie Rowe"] # Rätt svar är först i listan, Alternativ[0].
        print("Alternativ:")
        Alternativnr = random.randint(0, (len(Alternativ)-1)) # Svarsalternativet är ett slumpmässigt element i listan Alternativ.
        print("1: " + Alternativ[Alternativnr])
        Rätt_svar1 = 0 # Om svarsalternativet är det första elementet i listan har variabeln Rätt_svar1 värdet 1, annars är värdet 0.
        if Alternativnr == 0:
            Rätt_svar1 = 1
        del Alternativ[Alternativnr] # Svarsalternativet tas bort från listan Alternativ.

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("X: " + Alternativ[Alternativnr])
        Rätt_svarX = 0
        if Alternativnr == 0:
            Rätt_svarX = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("2: " + Alternativ[Alternativnr])

        Svar = str(input("Ange ditt svar: ")) # Tar emot svaret som en string.

        Alternativ = ["Lisa Marie Presley", "Priscilla Presley", "Debbie Rowe"] # Alla svarsalternativ läggs till i listan Alternativ igen.
        if Svar == "1" and Rätt_svar1 == 1: # Om svaret är 1 och Rätt_svar1 är 1 är svaret 1 rätt.
            print("Rätt!")
            Antal_poäng += 1 # Antal poäng adderas med 1.
        elif Svar == "1" and Rätt_svar1 != 1: # Om svaret är 1 och Rätt_svar1 inte är 1 är svaret fel.
            if Rätt_svarX == 1: # Om Rätt_svar1 inte är 1 och Rätt_svarX är 1 är rätt svar X.
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            else: # Om varken Rätt_svar1 eller Rätt_svarX är 1 skriver programmet är rätt svar 2 i terminalen.
                print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            
        elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
            if Rätt_svar1 == 1:
                print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")

        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1: # Om svaret inte är 1, X eller 2 påminns man om det.
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")

        Antal_frågor += 1
        print("Du har just nu " + str(Antal_poäng) + " poäng.")


    elif Frågenr == 2:
        print("")
        print("Fråga " + str(Antal_frågor + 1) + ": I vilket av följande länder finns floden Donau?")
        Alternativ = ["Kroatien", "Slovenien", "Bosnien-Hercegovina"]
        print("Alternativ:")
        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("1: " + Alternativ[Alternativnr])
        Rätt_svar1 = 0
        if Alternativnr == 0:
            Rätt_svar1 = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("X: " + Alternativ[Alternativnr])
        Rätt_svarX = 0
        if Alternativnr == 0:
            Rätt_svarX = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("2: " + Alternativ[Alternativnr])

        Svar = str(input("Ange ditt svar: "))

        Alternativ = ["Kroatien", "Slovenien", "Bosnien-Hercegovina"]
        if Svar == "1" and Rätt_svar1 == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "1" and Rätt_svar1 != 1:
            if Rätt_svarX == 1:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            
        elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
            if Rätt_svar1 == 1:
                print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")

        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")

        Antal_frågor += 1
        print("Du har just nu " + str(Antal_poäng) + " poäng.")


    elif Frågenr == 3:
        print("")
        print("Fråga " + str(Antal_frågor + 1) + ": Vad hette uppdraget som förde upp de första människorna till månen?")
        Alternativ = ["Apollo 11", "Apollo 12", "Apollo 13"]
        print("Alternativ:")
        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("1: " + Alternativ[Alternativnr])
        Rätt_svar1 = 0
        if Alternativnr == 0:
            Rätt_svar1 = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("X: " + Alternativ[Alternativnr])
        Rätt_svarX = 0
        if Alternativnr == 0:
            Rätt_svarX = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("2: " + Alternativ[Alternativnr])

        Svar = str(input("Ange ditt svar: "))

        Alternativ = ["Apollo 11", "Apollo 12", "Apollo 13"]
        if Svar == "1" and Rätt_svar1 == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "1" and Rätt_svar1 != 1:
            if Rätt_svarX == 1:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            
        elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
            if Rätt_svar1 == 1:
                print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")

        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")

        Antal_frågor += 1
        print("Du har just nu " + str(Antal_poäng) + " poäng.")

    elif Frågenr == 4:
        print("")
        print("Fråga " + str(Antal_frågor + 1) + ": År 1892 byggdes Sveriges första velodrom, i vilken stad?")
        Alternativ = ["Lund", "Malmö", "Helsingborg"]
        print("Alternativ:")
        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("1: " + Alternativ[Alternativnr])
        Rätt_svar1 = 0
        if Alternativnr == 0:
            Rätt_svar1 = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("X: " + Alternativ[Alternativnr])
        Rätt_svarX = 0
        if Alternativnr == 0:
            Rätt_svarX = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("2: " + Alternativ[Alternativnr])

        Svar = str(input("Ange ditt svar: "))

        Alternativ = ["Lund", "Malmö", "Helsingborg"]
        if Svar == "1" and Rätt_svar1 == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "1" and Rätt_svar1 != 1:
            if Rätt_svarX == 1:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            
        elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
            if Rätt_svar1 == 1:
                print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")

        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")

        Antal_frågor += 1
        print("Du har just nu " + str(Antal_poäng) + " poäng.")


    elif Frågenr == 5:
        print("")
        print("Fråga " + str(Antal_frågor + 1) + ": Vilket av följande bilmärken är inte tyskt?")
        Alternativ = ["Fiat", "Porsche", "BMW"]
        print("Alternativ:")
        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("1: " + Alternativ[Alternativnr])
        Rätt_svar1 = 0
        if Alternativnr == 0:
            Rätt_svar1 = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("X: " + Alternativ[Alternativnr])
        Rätt_svarX = 0
        if Alternativnr == 0:
            Rätt_svarX = 1
        del Alternativ[Alternativnr]

        Alternativnr = random.randint(0, (len(Alternativ)-1))
        print("2: " + Alternativ[Alternativnr])

        Svar = str(input("Ange ditt svar: "))

        Alternativ = ["Fiat", "Porsche", "BMW"]
        if Svar == "1" and Rätt_svar1 == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "1" and Rätt_svar1 != 1:
            if Rätt_svarX == 1:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

        if Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            
        elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Rätt!")
            Antal_poäng += 1
        elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
            if Rätt_svar1 == 1:
                print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            else:
                print("Fel, rätt svar är X, " + Alternativ[0] + ".")

        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")
        elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
            print("Kom ihåg att svara 1, X eller 2.")

        Antal_frågor += 1
        print("Du har just nu " + str(Antal_poäng) + " poäng.")


Frågenr = random.randint(1, 5) # Den sista frågan ställs precis som i while-loopen med de andra frågorna. Men det som skrivs i terminalen när man har svarat är annorlunda.
while Frågenr not in Frågor:
    Frågenr = random.randint(1, 5)

if Frågenr == 1:
    print("")
    print("Fråga " + str(Antal_frågor + 1) + ": Vem var Michael Jacksons första fru?")
    Alternativ = ["Lisa Marie Presley", "Priscilla Presley", "Debbie Rowe"] # Rätt svar är först i listan, Alternativ[0].
    print("Alternativ:")
    Alternativnr = random.randint(0, (len(Alternativ)-1)) # Svarsalternativet är ett slumpmässigt element i listan Alternativ.
    print("1: " + Alternativ[Alternativnr])
    Rätt_svar1 = 0 # Om svarsalternativet är det första elementet i listan har variabeln Rätt_svar1 värdet 1, annars är värdet 0.
    if Alternativnr == 0:
        Rätt_svar1 = 1
    del Alternativ[Alternativnr] # Svarsalternativet tas bort från listan Alternativ.

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("X: " + Alternativ[Alternativnr])
    Rätt_svarX = 0
    if Alternativnr == 0:
        Rätt_svarX = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("2: " + Alternativ[Alternativnr])

    Svar = str(input("Ange ditt svar: ")) # Tar emot svaret som en string.

    Alternativ = ["Lisa Marie Presley", "Priscilla Presley", "Debbie Rowe"] # Alla svarsalternativ läggs till i listan Alternativ igen.
    if Svar == "1" and Rätt_svar1 == 1: # Om svaret är 1 och Rätt_svar1 är 1 är svaret 1 rätt.
        print("Rätt!")
        Antal_poäng += 1 # Antal poäng adderas med 1.
    elif Svar == "1" and Rätt_svar1 != 1: # Om svaret är 1 och Rätt_svar1 inte är 1 är svaret fel.
        if Rätt_svarX == 1: # Om Rätt_svar1 inte är 1 och Rätt_svarX är 1 är rätt svar X.
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
        else: # Om varken Rätt_svar1 eller Rätt_svarX är 1 skriver programmet är rätt svar 2 i terminalen.
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
        
    elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
        if Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")

    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är X, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")


    Antal_frågor += 1
    print("Frågesporten är slut. Du fick " + str(Antal_poäng) + " av " + str(Antal_frågor) + " poäng.") # Skriver hur många poäng man fick.


elif Frågenr == 2:
    print("")
    print("Fråga " + str(Antal_frågor + 1) + ": I vilket av följande länder finns floden Donau?")
    Alternativ = ["Kroatien", "Slovenien", "Bosnien-Hercegovina"]
    print("Alternativ:")
    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("1: " + Alternativ[Alternativnr])
    Rätt_svar1 = 0
    if Alternativnr == 0:
        Rätt_svar1 = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("X: " + Alternativ[Alternativnr])
    Rätt_svarX = 0
    if Alternativnr == 0:
        Rätt_svarX = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("2: " + Alternativ[Alternativnr])

    Svar = str(input("Ange ditt svar: "))

    Alternativ = ["Kroatien", "Slovenien", "Bosnien-Hercegovina"]
    if Svar == "1" and Rätt_svar1 == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "1" and Rätt_svar1 != 1:
        if Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
        
    elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
        if Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")

    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är X, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    Antal_frågor += 1
    print("Frågesporten är slut. Du fick " + str(Antal_poäng) + " av " + str(Antal_frågor) + " poäng.") # Skriver hur många poäng man fick.


elif Frågenr == 3:
    print("")
    print("Fråga " + str(Antal_frågor + 1) + ": Vad hette uppdraget som förde upp de första människorna till månen?")
    Alternativ = ["Apollo 11", "Apollo 12", "Apollo 13"]
    print("Alternativ:")
    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("1: " + Alternativ[Alternativnr])
    Rätt_svar1 = 0
    if Alternativnr == 0:
        Rätt_svar1 = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("X: " + Alternativ[Alternativnr])
    Rätt_svarX = 0
    if Alternativnr == 0:
        Rätt_svarX = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("2: " + Alternativ[Alternativnr])

    Svar = str(input("Ange ditt svar: "))

    Alternativ = ["Apollo 11", "Apollo 12", "Apollo 13"]
    if Svar == "1" and Rätt_svar1 == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "1" and Rätt_svar1 != 1:
        if Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
        
    elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
        if Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")

    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är X, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    Antal_frågor += 1
    print("Frågesporten är slut. Du fick " + str(Antal_poäng) + " av " + str(Antal_frågor) + " poäng.") # Skriver hur många poäng man fick.

elif Frågenr == 4:
    print("")
    print("Fråga " + str(Antal_frågor + 1) + ": År 1892 byggdes Sveriges första velodrom, i vilken stad?")
    Alternativ = ["Lund", "Malmö", "Helsingborg"]
    print("Alternativ:")
    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("1: " + Alternativ[Alternativnr])
    Rätt_svar1 = 0
    if Alternativnr == 0:
        Rätt_svar1 = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("X: " + Alternativ[Alternativnr])
    Rätt_svarX = 0
    if Alternativnr == 0:
        Rätt_svarX = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("2: " + Alternativ[Alternativnr])

    Svar = str(input("Ange ditt svar: "))

    Alternativ = ["Lund", "Malmö", "Helsingborg"]
    if Svar == "1" and Rätt_svar1 == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "1" and Rätt_svar1 != 1:
        if Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
        
    elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
        if Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")

    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är X, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    Antal_frågor += 1
    print("Frågesporten är slut. Du fick " + str(Antal_poäng) + " av " + str(Antal_frågor) + " poäng.") # Skriver hur många poäng man fick.


elif Frågenr == 5:
    print("")
    print("Fråga " + str(Antal_frågor + 1) + ": Vilket av följande bilmärken är inte tyskt?")
    Alternativ = ["Fiat", "Porsche", "BMW"]
    print("Alternativ:")
    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("1: " + Alternativ[Alternativnr])
    Rätt_svar1 = 0
    if Alternativnr == 0:
        Rätt_svar1 = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("X: " + Alternativ[Alternativnr])
    Rätt_svarX = 0
    if Alternativnr == 0:
        Rätt_svarX = 1
    del Alternativ[Alternativnr]

    Alternativnr = random.randint(0, (len(Alternativ)-1))
    print("2: " + Alternativ[Alternativnr])

    Svar = str(input("Ange ditt svar: "))

    Alternativ = ["Fiat", "Porsche", "BMW"]
    if Svar == "1" and Rätt_svar1 == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "1" and Rätt_svar1 != 1:
        if Rätt_svarX == 1:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    if Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar.lower() == "x" and Rätt_svar1 == 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar.lower() == "x" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")
        
    elif Svar == "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Rätt!")
        Antal_poäng += 1
    elif Svar == "2" and (Rätt_svar1 == 1 or Rätt_svarX == 1):
        if Rätt_svar1 == 1:
            print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
        else:
            print("Fel, rätt svar är X, " + Alternativ[0] + ".")

    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 == 1:
        print("Fel, rätt svar är 1, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX == 1:
        print("Fel, rätt svar är X, " + Alternativ[0] + ".")
    elif Svar != "1" and Svar.lower != "x" and Svar != "2" and Rätt_svar1 != 1 and Rätt_svarX != 1:
        print("Fel, rätt svar är 2, " + Alternativ[0] + ".")

    Antal_frågor += 1
    print("Frågesporten är slut. Du fick " + str(Antal_poäng) + " av " + str(Antal_frågor) + " poäng.") # Skriver hur många poäng man fick.