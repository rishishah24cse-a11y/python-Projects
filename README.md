# Alexa Voice Assistant (Python)

## Overview

This project is a simple voice-controlled virtual assistant named **Alexa** built using Python. It can listen to voice commands, convert speech to text, open websites, perform Google searches, play YouTube videos, and execute basic system-related tasks.

Unlike traditional speech recognition projects that require **PyAudio**, this assistant records audio using the **sounddevice** library and then processes it using Google's Speech Recognition API.

---

# Features

* Voice-controlled interaction
* Text-to-Speech responses
* Open popular websites
* Search Google using voice commands
* Play YouTube videos using voice commands
* Open Google Classroom, Drive, GitHub, WhatsApp, Gmail, ChatGPT, Gemini, Claude, Instagram, etc.
* Exit the assistant using voice commands
* Works without PyAudio

---

# Libraries Used

## 1. speech_recognition

Used for converting speech into text.

```python
import speech_recognition as sr
```

Provides access to Google's Speech Recognition API.

---

## 2. pyttsx3

Used for Text-to-Speech conversion.

```python
import pyttsx3
```

Allows Alexa to speak responses back to the user.

---

## 3. pywhatkit

Used for:

* Playing YouTube videos
* Performing Google searches

```python
import pywhatkit
```

---

## 4. webbrowser

Used to open websites directly in the default browser.

```python
import webbrowser
```

---

## 5. sounddevice

Records microphone audio without requiring PyAudio.

```python
import sounddevice as sd
```

---

## 6. numpy

Used internally for handling audio data.

```python
import numpy as np
```

---

## 7. scipy.io.wavfile

Used to save recorded audio as a WAV file.

```python
from scipy.io.wavfile import write
```

---

## 8. tempfile

Creates temporary audio files.

```python
import tempfile
```

---

## 9. os

Used for file management operations.

```python
import os
```

---

# Code Explanation

## Voice Engine Initialization

```python
engine = pyttsx3.init()
```

Initializes the Text-to-Speech engine.

---

### Selecting Voice

```python
voices = engine.getProperty('voices')

if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
```

Chooses the second available voice (usually female).

---

### Setting Speech Properties

```python
engine.setProperty('rate', 180)
engine.setProperty('volume', 1)
```

* Rate = 180 words per minute
* Volume = Maximum (1)

---

# Speak Function

```python
def talk(text):
```

Purpose:

Converts text into speech.

### Working

```python
print("Alexa:", text)
```

Displays the response in the terminal.

```python
engine.say(text)
engine.runAndWait()
```

Speaks the response aloud.

---

# Audio Recording Function

```python
def record_audio(duration=10, fs=44100):
```

Purpose:

Records microphone input for 10 seconds.

### Parameters

* duration = Recording duration
* fs = Sampling rate (44100 Hz)

---

### Recording Audio

```python
recording = sd.rec(
    int(duration * fs),
    samplerate=fs,
    channels=1,
    dtype='int16'
)
```

Starts recording.

---

### Waiting for Completion

```python
sd.wait()
```

Waits until recording is finished.

---

### Creating Temporary File

```python
temp_file = tempfile.NamedTemporaryFile(
    delete=False,
    suffix=".wav"
)
```

Creates a temporary WAV file.

---

### Saving Audio

```python
write(temp_file.name, fs, recording)
```

Stores recorded audio in the file.

---

### Return File Path

```python
return temp_file.name
```

Returns the audio file location.

---

# Taking Voice Commands

```python
def take_command():
```

Purpose:

Converts spoken audio into text.

---

## Creating Recognizer

```python
recognizer = sr.Recognizer()
```

Creates a Speech Recognition object.

---

## Recording User Voice

```python
audio_file = record_audio()
```

Captures microphone input.

---

## Reading Audio File

```python
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)
```

Loads recorded audio.

---

## Speech Recognition

```python
command = recognizer.recognize_google(audio)
```

Uses Google's API to convert speech into text.

---

## Cleanup

```python
os.remove(audio_file)
```

Deletes temporary audio file.

---

## Convert to Lowercase

```python
command = command.lower()
```

Makes command matching easier.

---

## Wake Word Removal

```python
if "alexa" in command:
    command = command.replace("alexa", "").strip()
```

Removes the word "Alexa" from the command.

Example:

Input:

```text
Alexa open YouTube
```

Output:

```text
open youtube
```

---

# Error Handling

## Unknown Speech

```python
except sr.UnknownValueError:
```

When speech cannot be understood.

Response:

```text
Sorry, I could not understand.
```

---

## Internet Error

```python
except sr.RequestError:
```

When Google's Speech API cannot be reached.

Response:

```text
Internet connection problem.
```

---

# Command Processing

```python
def process_command(command):
```

This function decides what action to perform.

---

## Open Google Classroom

Command:

```text
open classroom
```

Action:

```python
webbrowser.open("https://classroom.google.com")
```

---

## Open YouTube

Command:

```text
open youtube
```

Opens YouTube.

Command:

```text
open youtube and play shape of you
```

Action:

```python
pywhatkit.playonyt(query)
```

Plays the requested video.

---

## Google Search

Command:

```text
open google and search python tutorial
```

Action:

```python
pywhatkit.search(query)
```

Searches Google.

---

## Open Claude

Command:

```text
open claude
```

Opens Claude AI.

---

## Open Settings

Command:

```text
open settings
```

Opens Windows Settings.

---

## Open Gemini

Command:

```text
open gemini
```

Opens Google's Gemini AI.

---

## Open Google Drive

Command:

```text
open google drive
```

Opens Google Drive.

---

## Open GitHub

Command:

```text
open github
```

Opens GitHub.

---

## Open WhatsApp

Command:

```text
open whatsapp
```

Opens WhatsApp Web.

---

## Open Gmail

Command:

```text
open email
```

or

```text
gmail
```

Opens Gmail.

---

## Open ChatGPT

Command:

```text
open chatgpt
```

Opens ChatGPT.

---

## Open Instagram

Command:

```text
open instagram
```

Opens Instagram.

---

# Exit Command

Commands:

```text
exit
```

or

```text
stop
```

Response:

```text
Goodbye
```

The assistant stops running.

---

# Main Function

```python
def main():
```

Controls the entire program.

---

## Welcome Message

```python
talk("Hello. I am Alexa. How can I help you?")
```

Greets the user.

---

## Continuous Listening Loop

```python
while running:
```

Keeps Alexa active.

---

### Listen for Command

```python
command = take_command()
```

Captures user speech.

---

### Execute Command

```python
running = process_command(command)
```

Processes the command.

If user says:

```text
exit
```

The loop ends.

---

# Program Flow

```text
Start Program
      ↓
Initialize Voice Engine
      ↓
Alexa Greets User
      ↓
Listen for Voice Input
      ↓
Convert Speech to Text
      ↓
Recognize Command
      ↓
Perform Action
      ↓
Speak Response
      ↓
Wait for Next Command
      ↓
Exit on "stop" or "exit"
```

---

# Future Improvements

* AI-powered conversations using OpenAI API
* Weather updates
* News reading
* Email sending
* Voice-controlled file management
* Desktop application launcher
* Face recognition login
* Smart home automation
* Custom wake-word detection
* Integration with Gemini, Claude, and ChatGPT APIs

---

# Author

Developed using Python with Speech Recognition, Text-to-Speech, and Web Automation technologies.

