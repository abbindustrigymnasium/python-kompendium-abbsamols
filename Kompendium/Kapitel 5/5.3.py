Norden = ["Sverige", "Norge", "Danmark", "Finland", "Island"]
Storbritannien = ["England", "Skottland", "Wales", "Nordirland"]

print("Ange ett land:")
Land = str(input())

if Land.title() in Norden: # Land.title() gör om str(input()) så att den första bokstaven blir en versal.
    print(Land.title() + " tillhör Norden.")

elif Land.title() in Norden:
    print(Land.title() + " tillhör Norden.")

else:
    print(Land.title() + " tillhör varken Norden eller Storbritannien.")