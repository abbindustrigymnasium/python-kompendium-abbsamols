mängd = range(500)
summa = 0

for nummer in mängd:
    if nummer % 2 != 0:
        summa += nummer # Alla nummer som inte har resten 0 om det divideras med 2 (är udda) summeras.

print (summa)