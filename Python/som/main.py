import os
import time
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from quickstar import autheticate_google, get_events

def speak(text):
    tts = gTTS(text = text, lang="pt-br")
    filename = "sound.mp3"
    tts.save(filename)
    playsound(filename)


def get_audio():
    
    r = sr.Recognizer()
    with sr.Microphone() as micro:
        r.adjust_for_ambient_noise(micro)
        print("Diga alguma coisa: ")
        audio = r.listen(micro)
        said = ""

        try:
            said = r.recognize_google(audio, language= "pt-br")
            print(said)
        except Exception as e:
            print("Exeption " + str(e))
    
    return  said.lower()

os.system("clear")
'''

text = ""
while (not "sair" in text):
    text = get_audio()
    if ("olá" in text):
        speak("Olá, o que você deseja")
    if ("nome" and "seu" in text):
        speak("meu nome é Jarvis")
    if ("nome" and "meu" in text):
        speak("Você é o Jamisson")
'''

service = autheticate_google()
get_events(service, 2)