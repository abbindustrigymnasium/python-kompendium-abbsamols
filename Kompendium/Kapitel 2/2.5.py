import math

print ("Hur många elever vill ha 2 vanliga korvar?")
Antal_elever_som_vill_ha_2_vanliga_korvar = int(input()) # Svaret tas emot som en int.

print ("Hur många elever vill ha 3 vanliga korvar?")
Antal_elever_som_vill_ha_3_vanliga_korvar = int(input()) # Svaret tas emot som en int.

print ("Hur många elever vill ha 2 veganska korvar?")
Antal_elever_som_vill_ha_2_veganska_korvar = int(input()) # Svaret tas emot som en int.

print ("Hur många elever vill ha 3 veganska korvar?")
Antal_elever_som_vill_ha_3_veganska_korvar = int(input()) # Svaret tas emot som en int.

# Beräknar antalet förpackningar med drycker och de olika korvsorterna.
Antal_förpackningar_med_vanliga_korvar = ((Antal_elever_som_vill_ha_3_vanliga_korvar * 0.375) + (Antal_elever_som_vill_ha_2_vanliga_korvar * 0.25))

Antal_förpackningar_med_veganska_korvar = ((Antal_elever_som_vill_ha_3_veganska_korvar * 0.75) + (Antal_elever_som_vill_ha_2_veganska_korvar * 0.5))

Antal_drycker = (Antal_elever_som_vill_ha_2_vanliga_korvar + Antal_elever_som_vill_ha_3_vanliga_korvar + Antal_elever_som_vill_ha_2_veganska_korvar + Antal_elever_som_vill_ha_3_veganska_korvar)

# Tack vare math.ceil avrundas antalet förpackniningar uppåt till närmsta heltal.
Total_kostnad = (math.ceil(Antal_förpackningar_med_vanliga_korvar) * 20.95) + (math.ceil(Antal_förpackningar_med_veganska_korvar) * 34.95) + (Antal_drycker * 13.95)

# Skriver vad som behöver köpas och den totala kostnaden.
print ("Inköpslista:")
print ("Vanlig korv: " + str(math.ceil(Antal_förpackningar_med_vanliga_korvar)) + " förpackningar")
print ("Vegansk korv: " + str(math.ceil(Antal_förpackningar_med_veganska_korvar)) + " förpackningar")
print ("Dryck: " + str(Antal_drycker) + " drickor")
print ("Total kostnad: " + str(Total_kostnad) + " SEK")