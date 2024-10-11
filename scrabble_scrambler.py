from pathlib import Path

print("Welcome to scrabble scrambler!", end="\n\n")

dictionaries = [f for f in Path().glob("*.txt")]

if not dictionaries:
    print("---")
    print("Please place the text files you'd like to use as dictionaries into the current directory.")
    print("Thereafter, please run the script again.")
    print("---", end="\n\n")
    quit()

selected_dictionary = 0    
if len(dictionaries) > 1:
    print("Please select the dictionary you'd like to use")
    for idx, dictionary in enumerate(dictionaries):
        print(f"{idx+1}. {dictionary}")

