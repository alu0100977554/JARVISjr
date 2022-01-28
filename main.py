from types import coroutine
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import openai

import chatbot

listener = sr.Recognizer()
engine = pyttsx3.init()

def change_voice(engine, language, gender='male'):
    for voice in engine.getProperty('voices'):
        if language in voice.id and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

def initial_setup():

    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1])
    wikipedia.set_lang('es')

    change_voice(engine, 'spanish')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-25)

    openai.api_key = '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'

def run_jarvis():
    initial_setup()

    talk('Hola, señor Stark')
    command = ''

    while command != 'apágate':
        try:
            command = take_command()

        except sr.UnknownValueError:
                listener = sr.Recognizer()
                continue

def talk(text, replaced_word=''):
    text = text.replace(replaced_word, '')
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def experimental_mode():
    talk('Modo experimental activado')
    with sr.Microphone() as audio:
        said = listener.listen(audio)

        command = listener.recognize_google(said, language='es-ES')
        command = command.lower()
        print(command)

        while command != 'entra en modo normal':
            response = openai.Completion.create(
                engine="davinci",
                prompt="",
                temperature=0.7,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            answer = response.choices[0].text.strip()
            talk(answer)

            said = listener.listen(audio)
            command = listener.recognize_google(said, language='es-ES')
            command = command.lower()
            print(command)

def take_command():
    with sr.Microphone() as audio:
        said = listener.listen(audio)

        command = listener.recognize_google(said, language='es-ES')
        command = command.lower()
        if 'yarbiss' in command:
            talk("Dígamelon")
            print('     Listening...')

            said = listener.listen(audio)
            command = listener.recognize_google(said, language='es-ES')
            command = command.lower()

            if 'reproduce' in command:
                talk('Reproduciendo' + command, 'reproduce')
                pywhatkit.playonyt(command)

            elif 'busca' in command:
                talk('Buscando: ' + command, 'busca')
                pywhatkit.search(command)

            elif 'hora' in command:
                time = datetime.datetime.now().strftime('%H:%M')
                talk('Son las ' + time)

            elif 'qué es' in command or 'quién' in command:
                command = command.replace('qué', '')
                command = command.replace('quién', '')
                try:
                    article = wikipedia.summary(command, 2)
                    talk(article)
                except:
                    talk('No he podido encontrar lo que buscaba')
            
            elif 'chiste' in command or 'broma' in command:
                talk(pyjokes.get_joke('es'))

            elif 'entra en modo sin barreras' in command:
                talk('Desactivando limitaciones de seguridad')
                experimental_mode()
            
            else:
                talk('No he podido entenderle, señor Stark.')
        
        else:
            ints = chatbot.predict_class(command)
            res = chatbot.get_response(ints)
            talk(res)
            
        return command
                    

run_jarvis()