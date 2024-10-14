from pathlib import Path
from helper_functions import sentence_scrambler, dictionary_to_word_length_map

print("Welcome to scrabble scrambler!", end="\n\n")

dictionaries = [f for f in Path().glob("*.txt")]
if not dictionaries:
    print("---")
    print("Please place the text files you'd like to use as dictionaries into the current directory.")
    print("Thereafter, please run the script again.")
    print("---", end="\n\n")
    quit()

selected_dictionary = None
if len(dictionaries) > 1:
    dictionary_range = list(range(0, len(dictionaries)))
    while selected_dictionary not in dictionary_range:
        for idx, dictionary in enumerate(dictionaries):
            print(f"{idx}. {dictionary}")    
        try:
            selected_dictionary = int(input("Please select the dictionary you'd like to use: "))
        except ValueError:
            print("that input is invalid, please try again")
else:
     selected_dictionary = 0   

dictionary = dictionaries[selected_dictionary]
words_by_length = dictionary_to_word_length_map(dictionary)
        
sentence = ""
while True:
    sentence = input("Please input the sentence you'd like to convert ('_q to exit'): ")
    if sentence == "_q":
        break
    
    print(sentence_scrambler(sentence, words_by_length), end="\n\n")

print("---")    
print("Thanks for using Scrabble Scrambler")
quit()    
