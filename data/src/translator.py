import json

with open("../data/dictionary.json") as f:
    dictionary = json.load(f)

def translate_word(word):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]["gondi"]
    return word

def translate_sentence(sentence):
    words = sentence.split()
    translated = [translate_word(w) for w in words]
    return " ".join(translated)

print(translate_sentence("I eat rice"))
