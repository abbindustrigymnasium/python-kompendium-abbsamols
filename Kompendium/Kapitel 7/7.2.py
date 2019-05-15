import random

print ("THE HIGHER LOWER GAME")
print ("---------------------")
print ("Welcome to The Higher Lower Game. I will randomise a number between 0 and 99. Can you guess it?")
print ("-----------------------------------------------------------------------------------------------")

for x in range(100): # Programmet får ett slumpmässigt tal som anväändaren ska gissa.
  x = random.randint(0,99)

Number = x
Number_of_guesses = 0

while True:
    Guess = int(input()) # Om gissningen stämmer meddelas det enligt exempellösningen.
    if Guess == Number:
        print (str(Guess) + " is correct!")
        print ("It took you " + str(Number_of_guesses) + " guesses.") # Det skrivs hur många gissningar det krävdes för att gissa rätt.
        print ("Good job!")
        break
    else:
        if Guess < Number: # Om gissningen är mindre än det slumpmässiga talet skrivs det att man ska gissa på ett större tal.
            print ("HIGHER!")
            print ("Try again!")
            Number_of_guesses += 1
            continue
        else: # Om gissningen är större än det slumpmässiga talet skrivs det att man ska gissa på ett mindre tal.
            print ("LOWER!")
            print ("Try again!")
            Number_of_guesses += 1
            continue