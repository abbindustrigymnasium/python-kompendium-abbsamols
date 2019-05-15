# Elementen i sömnbehov ligger i åldersordning och börjar med sömnbehovet vid åldern 1 år.
Sömnbehov = ["14", "13", "12", "11,5", "11", "11", "10,5", "10", "10", "10", "9,5", "9", "9", "9", "9", "8,5"]

print("Ange ditt namn:")
Namn = str(input())
print("Ange din ålder:")
Ålder = int(input())

if Ålder < 17: # Om man är yngre än 17 år skrivs sömnbehovet ut enligt listan "Sömnbehov".
    print("Hallå " + Namn + "! Enligt Vårdguidens rekommendationer behöver individer i din ålder (" + str(Ålder) + ") år sova minst " + Sömnbehov[Ålder-1] +" timmar per natt.")

else: #Om man är äldre än 16 år är sömnbehovet 8 timmar.
    print("Hallå " + Namn + "! Enligt Vårdguidens rekommendationer behöver individer i din ålder (" + str(Ålder) + ") år sova minst 8 timmar per natt.")