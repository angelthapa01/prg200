import math

# this program analyses temperature readings from a weather station

station_name = "Kathmandu Weather Station"

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]


def get_average(temps):
    return sum(temps) / len(temps)


def get_deviation(temps):
    mean = get_average(temps)

    variance = 0

    # calculate variance
    for temp in temps:
        variance += (temp - mean) ** 2

    variance = variance / len(temps)

    return math.sqrt(variance)


def get_summary(temps):
    print("station:", station_name)
    print("minimum temperature:", min(temps))
    print("maximum temperature:", max(temps))
    print("average temperature:", round(get_average(temps), 2))
    print("standard deviation:", round(get_deviation(temps), 2))


get_summary(temperatures)

# mean is a local variable and cannot be used outside the function
# print(mean)