def get_day_name(day_num):

    days = ['пятница', 'суббота', 'воскресенье', 'понедельник', 'вторник', 'среда', 'четверг']
    return days[(day_num - 1) % 7]


def main():

    input_day = int(input("Введите число дня месяца (от 1 до 30): "))


    if not (1 <= input_day <= 30):
        print("Число должно быть в диапазоне от 1 до 30")
        return


    day_name = get_day_name(input_day)
    print(f"Название дня месяца: {day_name}")


if __name__ == "__main__":
    main()