def get_day_name(day_num, language):

    days_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_ru = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    if language == 'en':
        return days_en[day_num]
    elif language == 'ru':
        return days_ru[day_num]


def main():

    input_list = input("Введите список в формате 'номер_дня язык': ").split()
    days = []

    for item in input_list:
        day_num, language = item.split()
        days.append((int(day_num), language))


    for day_num, language in days:
        day_name = get_day_name(day_num, language)
        print(f"День {day_num} на {language}: {day_name}")


if __name__ == "__main__":
    main()