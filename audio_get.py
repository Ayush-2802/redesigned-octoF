import speech_recognition as sr
import os

def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source, phrase_time_limit=5)
    print("Stop.")

    # noinspection PyBroadException
    try:
        text_: str = r.recognize_google(audio, language='en-US')
        print("Operator : ", text_)
        return text_

    except:
        assistant_speaks('''Could not understand your audio, due to no internet connection.
          please check the connection and try again ''')
        return
