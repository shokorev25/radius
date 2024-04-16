import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    radius = float(input("Введите радиус круга: "))
    area = calculate_circle_area(radius)
    print("Площадь круга с радиусом", radius, "равна", area)
