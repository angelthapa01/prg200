pi = 3.14

def circle_area(radius):
    return pi * radius ** 2

def circle_perimeter(radius):
    return 2 * pi * radius

radius = float(input("Enter radius: "))

print("Area =", circle_area(radius))
print("Perimeter =", circle_perimeter(radius))