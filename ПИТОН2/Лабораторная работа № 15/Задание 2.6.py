def print_or_add_phrase(phrase, phrases):

    if phrase in phrases:
        print(phrase)
    else:
        phrases.append(phrase)
        print("Фраза добавлена в список")


def main():

    input_phrases = input("Введите список фраз через пробел: ").split()
    phrases = [phrase.strip() for phrase in input_phrases]


    input_phrase = input("Введите фразу: ")

    
    print_or_add_phrase(input_phrase, phrases)


if __name__ == "__main__":
    main()