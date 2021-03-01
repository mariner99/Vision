#For playing the audio without saving any file, gTTS requires a file to be saved.
import os
from gtts import gTTS
from playsound import playsound

# Function for Text to Speech
def t2s(text):
    tts = gTTS(text,lang='en', tld='fr')
    tts.save("input.mp3")
    playsound('input.mp3')

#File location is an issue
















