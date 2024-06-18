def create_letter_frequency_dict(word):

    frequency_dict = {}
    for letter in word:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    return frequency_dict



input_string = "hello"
frequency_dict = create_letter_frequency_dict(input_string)
print(frequency_dict)