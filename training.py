import json
import json

import nltk                                 #natural language tool kit
from nltk.stem import WordNetLemmatizer     # Herramienta para identificar variaciones de una palabra

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())       # Diccionario

words = []
classes = []
documents = []
ignore_letters = ['¿', '?', '¡', '!', ',', '.']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)         # Convierte cada palabra de "patterns" en un token
        words.extend(word_list)
        documents.append((word_list, intent['tag']))    # Cada frase con el "tag" correspondiente

        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)