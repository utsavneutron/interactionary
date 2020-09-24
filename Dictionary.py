import json

data = json.load(open("data.json"))


def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it"


word = ""

while (word != "/end"):
    word = input("Enter a word: ")
    print(search(word))

    if(word == "/end"):
        print("Thank you for using the dictionary")
