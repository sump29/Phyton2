def transliterate(text):
    

    transliteration_map = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
        'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
        'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH',
        'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Ъ': '', 'Ь': '', 'Э': 'E',
        'Ю': 'IU', 'Я': 'IA'
    }

    result = ""
    for char in text:
        if char in transliteration_map:
            result += transliteration_map[char]
        else:
            result += char

    return result


# Пример использования функции
text = "Привет, мир!"
transliterated_text = transliterate(text)
print(transliterated_text)