male = [ # Skapar lista med män.
"Erik",
"Lars",
"Karl",
"Anders",
"Johan"
]
female = [ # Skapar lista med kvinnor.
"Maria",
"Anna",
"Margareta",
"Elisabeth",
"Eva"
]

print ("Vilket namn ska plockas bort från listorna?")
namn = str(input())

if namn in male:
    male.remove(namn) # Om namnet finns i listan "male" ska det tas bort därifrån.

elif namn in female:
    female.remove(namn) # Om namnet finns i listan "female" ska det tas bort därifrån.

print ("Män:", male)
print ("Kvinnor:", female)