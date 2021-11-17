import json

data = json.load(open("dictionary.json"))

def translate(word):
    word = word.lower() #converts word to lower case
    if word in data: #checks if word exists in lower case
        return data[word]
    elif word.title() in data: #checks if word exists in title case
        return data[word.title()]
    elif word.upper() in data: #checks if word exists in Upper case
        return data[word.upper()]
    else:
        print('You have entered the wrong word')

word = input("Enter the word you want to search")
output = translate(word)
print(output)
