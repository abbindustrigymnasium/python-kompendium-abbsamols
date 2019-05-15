import ui

# I terminalen skrivs text och tecken enligt ui.py-.
ui.line() # Skriver en rad med "-".
ui.header("EXEMPEL")
ui.line(True) # Skriver ut en rad med "-".
ui.echo("Detta är ett exempel på hur ett gränsnitt kan se ut.")
ui.line ()
ui.header ("Vad vill du göra?")
ui.line ()
ui.echo ("A | Visa inköpslista")
ui.echo ("B | Lägg till vara")
ui.echo ("C | Ta bort vara")
ui.echo ("X | Stäng programmet")
ui.line ()
ui.prompt("Val ")