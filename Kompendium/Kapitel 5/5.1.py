Daniel_Radcliffe = ["Man", "Brun", "Brun", "Daniel Radcliffe"]
Rupert_Grint = ["Man", "Röd", "Blå", "Rupert Grint"]
Emma_Watson = ["Kvinna", "Brun", "Brun", "Emma Watson"]
Selena_Gomez = ["Kvinna", "Brun", "Brun", "Selena Gomez"]
Samuel_Olsson = ["Man", "Brun", "Grön", "Samuel Olsson"]
Donald_Trump = ["Man", "Blond", "Grön", "Donald Trump"]
Stefan_Löfven = ["Man", "Brun", "Blå", "Stefan Löfven"]
Ulf_Kristersson = ["Man", "Svart", "Blå", "Ulf Kristersson"]
Jan_Björklund = ["Man", "Grå", "Blå", "Jan Björklund"]
Kändisar = [Daniel_Radcliffe, Rupert_Grint, Emma_Watson, Selena_Gomez, Samuel_Olsson, Donald_Trump, Stefan_Löfven, Ulf_Kristersson, Jan_Björklund]
Liknade_kändisar = ""

print("Ange kön:")
Kön = str(input())

print("Ange hårfärg:")
Hårfärg = str(input())

print("Ange ögonfärg:")
Ögonfärg = str(input())

for Kändisar in Kändisar:
    if Kändisar[0] == Kön:
        if Kändisar[1] == Hårfärg:
            if Kändisar[2] == Ögonfärg:
                Liknade_kändisar += Kändisar[3] + ", " # Kändisar som har samma egenskap inom någon av variablerna läggs till i listan med liknande kändisar.

if Liknade_kändisar == "":
    print("Du liknar ingen kändis.")
else:
    print("Egenskaperna matchar med: " + Liknade_kändisar + ".") # Om man har minst en egenskap gemensam med en kändis skrivs kändisens eller kändisarnas namn.