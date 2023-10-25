import pyttsx3

def assistant_speaks(output):
    print("FRIDAY : ", output)
    engine = pyttsx3.init('sapi5')
    rate = engine.getProperty('rate')
    # noinspection PyTypeChecker
    engine.setProperty('rate', rate - 30)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(output)
    engine.runAndWait()
