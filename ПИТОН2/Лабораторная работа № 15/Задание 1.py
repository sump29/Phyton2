import math

def S(r):

    return math.pi * r ** 2

def l(r):

    return 2 * math.pi * r

def krug():

    radius = float(input("Введите радиус окружности: "))
    area = S(radius)
    circumference = l(radius)
    print(f"Площадь круга: {area:.2f} Длина окружности: {circumference:.2f}")


krug()