# Taxi Fare Calculator

trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

print("Taxi Fare Report")


# checking each trip
for trip in trips:

    distance = trip["distance"]
    hour = trip["hour"]

    # base fare
    fare = 150

    # fare for next 8 km
    if distance > 2 and distance <= 10:
        fare = fare + ((distance - 2) * 35)

    # fare beyond 10 km
    elif distance > 10:
        fare = fare + (8 * 35)
        fare = fare + ((distance - 10) * 28)

    # night surcharge
    if hour >= 22 or hour < 5:
        fare = fare + (fare * 0.10)

    # displaying result
    print("Distance:", distance, "km")
    print("Hour:", hour)
    print("Total Fare: NPR", fare)
  