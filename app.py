import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    #for words like Paris, Delhi, Texas, etc., title()
    elif word.title() in data:
        return data[word.title()]
    #for acronyms such as USA, upper()
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:            
        notes = str(input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0]))
        if notes == "Y".lower():
            return data[get_close_matches(word, data.keys())[0]]
        elif notes == "N".lower():
            return "Please try again."
        else:
            return "Your entry was not understood. Please try again."
    else:
        return "The word you entered does not appear to exist. Please double check it."


def user_search():
    text = str(input("Please enter a word to define: "))
    output = translate(text)
    if type(output) == list:
        for item in output:
            return item



print(user_search())
