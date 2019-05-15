Startnummer = int(input("Ange multiplikationstabell: "))
Nummer = 0
Antal_gånger_startnumret_har_adderats = 0


while Antal_gånger_startnumret_har_adderats < 4:
    Nummer += Startnummer # Talet ökar alltid med startnumret enligt multiplikationstabellen.
    print (Nummer)
    Antal_gånger_startnumret_har_adderats += 1

    if Antal_gånger_startnumret_har_adderats == 3: # När tre tal från multiplikationstabellen har skrivits ut frågas det om användaren vill att ytterligare tre tal ska skrivas ut.
        print ("Fortsätt?")
        Svar = str(input())
        if Svar.title() == "Ja":
            Antal_gånger_startnumret_har_adderats = 0
            continue

        else:
            break
    else: # Om inte tre tal från multiplikationstabellen har skrivits ska det skrivas minst ett tal till.
        continue