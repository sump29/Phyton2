def create_sentence_by_numbers(numbers_str, words_str):
    numbers = list(map(int, numbers_str.split()))
    words = words_str.split()

    sentence_words = [words[num - 1] for num in numbers]
    sentence = " ".join(sentence_words)
    sentence = sentence[0].upper() + sentence[1:]

    return sentence


numbers_str = input("Введите нумерацию слов:")
words_str = input("Введите слова согласно их количеству:")

result_sentence = create_sentence_by_numbers(numbers_str, words_str)
print(result_sentence)