import json
import random
import numpy as np

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


words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))                              # Eliminar posibles duplicados
classes = sorted(set(classes))

# El siguiente paso consiste en asignar valores numéricos a cada palabra,
# para que la red neuronal pueda realizar las operaciones correspondientes

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1          
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

training_x = list(training[:, 0])
training_y = list(training[:, 1])