def country_city_dict(n, country_data):

    country_city = {}
    for data in country_data:
        country, *cities = data.split(',')
        if country not in country_city:
            country_city[country] = []
        country_city[country].extend(cities)
    return country_city


def find_country(city, country_city_dict):

    for country, cities in country_city_dict.items():
        if city in cities:
            return country
    return ""



n = int(input("Введите количество стран: "))
country_data = [input(f"Введите города для страны {i + 1} (разделите запятыми): ").strip() for i in range(n)]
city_query = input("Введите город для поиска страны: ").strip()


country_city = country_city_dict(n, country_data)


country = find_country(city_query, country_city)


print(country or "Город не найден")