import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(input_word):
    # lower case all the input string provided
    input_word = input_word.lower()

    if input_word in data:
        return data[input_word]
    elif len(get_close_matches(input_word, data.keys())) > 0:
        choice = input("Did You mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(
            input_word, data.keys())[0])
        if choice == 'Y':
            return data[get_close_matches(input_word, data.keys())[0]]
        elif choice == 'N':
            return "The word doesn't exist . Please double check the word"
        else:
            return "We did not understand your entry"
    else:
        return "The word does'nt exist.Please check it again!."


word = input("Enter word: ")
print(translate(word))



