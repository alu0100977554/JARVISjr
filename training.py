import json
import random
import numpy as np

import pickle
import nltk                                 #natural language tool kit
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import optimizers     # Herramienta para identificar variaciones de una palabra

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.python.util import nest

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

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))
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

# Modelado de la red neuronal
model = Sequential()
model.add(Dense(128, input_shape=(len(training_x[0]),), activation='relu')) # 128 neuronas, nº de entradas de cada neurona = nº de palabras contenidas en bag
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))                                    # El nº de entradas es igual al nº de neuronas de la capa anterior
model.add(Dropout(0.5))
model.add(Dense(len(training_y[0]), activation='softmax'))                 # nº de neurnonas de esta capa debe ser igual al nº de resultados finales

sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)                #Optimizer
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(training_x), np.array(training_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.model', hist)
print("Done")