def is_triangle(sides):

    if len(sides) != 3:
        return False

    a, b, c = sides
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def main():

    input_sides = input("Введите длины отрезков через пробел: ").split()
    sides = [float(side) for side in input_sides]


    if is_triangle(sides):
        print("Это треугольник")
    else:
        print("Это не треугольник")


if __name__ == "__main__":
    main()