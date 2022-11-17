import json

list_of_words = []

with open('cenz/cenz.txt', encoding='utf-8') as file:
    for line in file:
        word = line.split('\n')[0]
        if word != '':
            list_of_words.append(word)

with open('cenz/cenz.json', 'w', encoding='utf-8') as js_file:
    json.dump(list_of_words, js_file)

