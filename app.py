import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(input_word):
    # lower case all the input string provided
    input_word = input_word.lower()

    if input_word in data:
        return data[input_word]
    elif len(get_close_matches(input_word, data.keys())) > 0:
        return "You mean %s instead" % get_close_matches(input_word, data.keys())[0]
    else:
        return "The word does'nt exist.Please check it again!."


word = input("Enter word: ")
print(translate(word))



