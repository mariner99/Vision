#For playing the audio without saving any file, gTTS requires a file to be saved.
import pyttsx3

# Function for Text to Speech
def t2s(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()





