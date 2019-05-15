print ("Hur gammal är du?")
Ålder = int(input()) # Svaret tas emot som en string.
År_till_myndig = 18 - Ålder
År_från_myndig = Ålder - 18
if Ålder < 18:
    print ("Du är myndig inom " + str(År_till_myndig) + " år!") # Skriver inom hur många år man blir myndig.
elif Ålder == 18:
    print ("Du har varit myndig i max ett år!")
elif Ålder > 18:
    print ("Du blev myndig för " + str(År_från_myndig) + " år sen!") # Skriver för hur många år sen man blev myndig.