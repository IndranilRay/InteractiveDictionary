import json

data = json.load(open("data.json"))


def translate(input_word):
    # lower case all the input string provided

    input_word = input_word.lower()

    if input_word in data:
        return data[input_word]
    else:
        return "The word does'nt exist.Please check it again!."


word = input("Enter word: ")
print(translate(word))



