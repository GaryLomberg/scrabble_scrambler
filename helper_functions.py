import random
from string import ascii_lowercase


def sentence_scrambler(sentence, words_by_length):
    """
    Step through each word in the sentence
    Use the word length map to find the list of words with matching length
    If found, add a random entry of matching length to the new sentence list
    """
    
    sentence_list = sentence.split()
    new_sentence_list = []
    
    for word in sentence_list:
        first_letter = word[0]
        length = len(word)
        letter = words_by_length.get(first_letter)
        if not letter:
            new_sentence_list.append(word)
            continue

        word_options = letter.get(length)
        if not word_options:
            new_sentence_list.append(word)
            continue

        random_word = word_options[random.randint(0, len(word_options) -1)]
        new_sentence_list.append(random_word)

    return " ".join(new_sentence_list)


def dictionary_to_word_length_map(dictionary):
    """
    Take a dictionary file as an argument
    Read the file and organise words by letter
    Thereafter organise words by count under each letter
    This is done for efficient lookup
    """
    
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
