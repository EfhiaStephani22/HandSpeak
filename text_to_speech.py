import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

last_spoken = ""
last_time = 0

def speak(text):
    global last_spoken, last_time
    current_time = time.time()

    if text != last_spoken and text != "Unknown Gesture" and current_time - last_time > 1.2:
        engine.say(text)
        engine.runAndWait()
        last_spoken = text
        last_time = current_time



