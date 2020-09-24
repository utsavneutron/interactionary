import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yes = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                    get_close_matches(word, data.keys())[0])
        if yes == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yes == "N":
            return "The Word is not in the dictionary. Are you sure it's not a slang?"
        else:
            return "We didn't undestand the word"
    else:
        return "The word doesn't exist. Please double check it"


word = ""

while (word != "/end"):
    word = input("Enter a word: ")
    if(word == "/end"):
        print("Thank you for using the dictionary")
        break
    print(search(word))
