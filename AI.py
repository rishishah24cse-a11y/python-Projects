import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
import os

# -----------------------------
# Voice Engine
# -----------------------------
engine = pyttsx3.init()

voices = engine.getProperty('voices')

if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 180)
engine.setProperty('volume', 1)

# -----------------------------
# Speak Function
# -----------------------------
def talk(text):
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# Record Audio without PyAudio
# -----------------------------
def record_audio(duration=10, fs=44100):

    print("Listening...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype='int16'
    )

    sd.wait()

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    write(temp_file.name, fs, recording)

    return temp_file.name

# -----------------------------
# Take Command
# -----------------------------
def take_command():

    recognizer = sr.Recognizer()

    try:

        audio_file = record_audio()

        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

        command = recognizer.recognize_google(audio)

        os.remove(audio_file)

        command = command.lower()

        print("You:", command)

        if "alexa" in command:
            command = command.replace("alexa", "").strip()

        return command

    except sr.UnknownValueError:
        talk("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        talk("Internet connection problem.")
        return ""

    except Exception as e:
        print(e)
        return ""


def process_command(command):

    if not command:
        return True

    if "open classroom" in command:
        talk("Opening Google Classroom")
        webbrowser.open("https://classroom.google.com")

    
    elif "open youtube" in command:
        query = command.replace("open youtube and play", "").strip()
        if query:
            talk(f"Playing:{query}")
            pywhatkit.playonyt(query)
        else:
            webbrowser.open("https://youtube.com")

    elif "open google" in command:
        query = command.replace("open google and search", "").strip()
        if query:
            talk(f"Search:{query}")
            pywhatkit.search(query)
        else:
            webbrowser.open("https://google.com")

    elif "open claude" in command:
        talk("Opening Claude")
        webbrowser.open("https://claude.ai")

    elif "open settings" in command:
        talk("Opening Settings")
        webbrowser.open("ms-settings:")

    elif "open gemini" in command:
        talk("Opening Gemini")
        webbrowser.open("https://gemini.google.com")

    elif "open google drive" in command:
        talk("Opening Google Drive")
        webbrowser.open("https://drive.google.com")


    elif "open github" in command:
        talk("Opening GitHub")
        webbrowser.open("https://github.com")
            
    
    elif "open whatsapp" in command:
        talk("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")


    elif "open email" in command or "gmail" in command:
        talk("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    
    elif "open chatgpt" in command:
        talk("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    elif "open instagram" in command:
        talk("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open github" in command:
        talk("Opening GitHub")
        webbrowser.open("https://github.com")


    elif "exit" in command or "stop" in command:
        talk("Goodbye")
        return False
    else:
        talk("Command not recognized.")
    return True

def main():
    talk("Hello. I am Alexa. How can I help you?")
    running = True
    while running:
        command = take_command()
        running = process_command(command)

if __name__ == "__main__":
    main()



