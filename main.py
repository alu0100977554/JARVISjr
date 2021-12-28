from types import coroutine
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import platform

listener = sr.Recognizer()
engine = pyttsx3.init()

clear_f = 'clear'

def change_voice(engine, language, gender='male'):
    for voice in engine.getProperty('voices'):
        if language in voice.id and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

def initial_setup():
    if platform.system() == 'Windows':
        clear_f = 'cls'

    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1])
    wikipedia.set_lang('es')
    change_voice(engine, 'spanish')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-25)

def run_jarvis():
    initial_setup()

    talk('Hola, señor Stark')

    while True:
        try:
            take_command()

        except sr.UnknownValueError:
                listener = sr.Recognizer()
                continue

def talk(text, replaced_word=''):
    text = text.replace(replaced_word, '')
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as audio:
        said = listener.listen(audio)

        command = listener.recognize_google(said, language='es-ES')
        command = command.lower()
        if 'yarbiss' in command:
            talk("digamelon")
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

            elif 'qué' in command or 'quién' in command:
                command = command.replace('qué', '')
                command = command.replace('quién', '')
                try:
                    article = wikipedia.summary(command, 2)
                    talk(article)
                except:
                    talk('No he podido encontrar lo que buscabas')
            
            elif 'chiste' in command or 'broma' in command:
                talk(pyjokes.get_joke('es'))

            elif 'apágate' in command:
                return
            
            else:
                talk('No he podido entenderte.')
                    

run_jarvis()