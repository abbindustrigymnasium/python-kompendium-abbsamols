def line(boolean = False):
    if boolean == True:
        print("******************************")
    else:
        print("------------------------------")

def header(string): # Inställningar för titel.
    string = string.center(26)
    print("| " + string)

# Inställningar för de andra typerna av text.
def echo(string):
    print("| " + string)

def prompt(string):
    return input("| " + string)