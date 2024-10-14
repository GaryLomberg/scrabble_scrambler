from pathlib import Path
from helper_functions import sentence_scrambler, dictionary_to_word_length_map

print("Welcome to scrabble scrambler!", end="\n\n")

# create list of text files in the cwd
# with the assumption that the file is a dictionary
dictionaries = [f for f in Path().glob("*.txt")]

# quit the script if no dictionaries found in the folder
if not dictionaries:
    print("---")
    print("Please place the text files you'd like to use as dictionaries into the current directory.")
    print("Thereafter, please run the script again.")
    print("---", end="\n\n")
    quit()

# allow the user to select a dictionary if multiple are in the folder
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
# Nice To Have: save the words_by_length data structure to a pickle file for next time
# The speed of processing at current dictionary size, means the process saving would
# be negligable though

# Main loop for  getting user sentence
sentence = ""
while True:
    sentence = input("Please input the sentence you'd like to convert ('_q to exit'): ")
    if sentence == "_q":
        break
    
    print(sentence_scrambler(sentence, words_by_length), end="\n\n")
    # sentence_scrambler function description in docstring

print("---")    
print("Thanks for using Scrabble Scrambler")
quit()    
