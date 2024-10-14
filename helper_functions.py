import random
from string import ascii_lowercase


def sentence_scrambler(sentence, words_by_length):
    sentence_list = sentence.split()
    new_sentence_list = []
    error_string = "Incompatible sentence / dictionary combination, please try again..."
    
    for word in sentence_list:
        first_letter = word[0]
        length = len(word)
        letter = words_by_length.get(first_letter)
        if not letter:
            return error_string

        word_options = letter.get(length)
        if not word_options:
            return error_string

        random_word = word_options[random.randint(0, len(word_options) -1)]
        new_sentence_list.append(random_word)

    return " ".join(new_sentence_list)


def dictionary_to_word_length_map(dictionary):
    words = []
    with open(dictionary) as d_file:
        words = d_file.read().splitlines()

    words_by_letter = {letter: [] for letter in ascii_lowercase}
    for word in words:
        words_by_letter[word[0]].append(word)

    words_by_length = {letter: {} for letter in ascii_lowercase}
    for letter, count_map in words_by_length.items():
        words = words_by_letter[letter]
        for word in words:
            if not count_map.get(len(word)):
                count_map[len(word)] = []
            count_map[len(word)].append(word)

    return words_by_length
