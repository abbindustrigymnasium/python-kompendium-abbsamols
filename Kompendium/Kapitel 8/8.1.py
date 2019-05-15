Distance = input("Ange distans: ") # Tar emot en distans i enheten kilometer eller miles.

def km_to_miles(dist):
    return str(dist * 0.621371192) + "miles" # Om distansen är i kilometer är längden 0.621371192 gånger så stor i miles.

def miles_to_km(dist):
    return str(dist * 1.609344) + "km" # Om distansen är i miles är längden 1.609344 gånger så stor i kilometer.

if "km" in Distance.lower():
    Distance2 = km_to_miles(float(Distance.strip("km"))) # Distance2 är distansen i den andra enheten.

elif "miles" in Distance.lower():
    Distance2 = miles_to_km(float(Distance.strip("miles")))

print (Distance + " motsvarar " + Distance2)