from gtts import gTTS
import playsound
import os
import time
def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech = gTTS(text)

    # Save the audio file to a temporary file
    speech_file = 'speech1.mp3'
    speech.save(speech_file)
    return speech_file

def play_audio(file):
    # Play the audio file
    # os.system('start ' + file)
    playsound.playsound(file)