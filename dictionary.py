import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(word):
    word = word.lower() #converts word to lower case
    if word in data: #checks if word exists in lower case
        return data[word]
    elif word.title() in data: #checks if word exists in title case
        return data[word.title()]
    elif word.upper() in data: #checks if word exists in Upper case
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes and n for no")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("oops")
        else:
            return("You have entered wrong input, please enter y or n")
    else:
        print('You have entered the wrong word')

word = input("Enter the word you want to search")
output = translate(word)
if type(output) == list:  #Cleans the output and gives it in a nice formatted way
    for item in output:
        print(item)
else:
    print(output)
