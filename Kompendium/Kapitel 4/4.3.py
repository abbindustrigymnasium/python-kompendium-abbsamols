registrerade =[" Anna ", "Eva ", " Erik ", " Lars ", " Karl "]
avanmälningar =[" Anna ", " Erik ", " Karl "]

for namn in avanmälningar:
    registrerade.remove(namn) # Namnen som finns med i listan "avanmälningar" tas bort från listan "registrerade".

print (registrerade)