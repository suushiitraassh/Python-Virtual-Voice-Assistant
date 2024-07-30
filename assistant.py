import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    greeting = ""
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    return greeting + " Welcome, I am your personal Google Assistant"

def VoiceCommand():
    r = sr.Recognizer()
    response_text.insert(tk.END, "Listening...\n")
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        response_text.insert(tk.END, "Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        response_text.insert(tk.END, f"User said: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        response_text.insert(tk.END, "Unable to Recognize your voice.\n")
        return "None"

def process_command(command):
    if 'hello' in command:
        response_text.insert(tk.END, 'Hi, how can I help you?\n')
        speak('Hi, how can I help you?')
    elif "wikipedia" in command:
        response_text.insert(tk.END, "Searching Wikipedia...\n")
        speak("Searching Wikipedia...")
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        response_text.insert(tk.END, f"According to Wikipedia:\n{results}\n")
        speak("According to Wikipedia")
        speak(results)
    elif 'open notepad' in command:
        response_text.insert(tk.END, 'Opening Notepad for you...\n')
        speak('Opening Notepad for you...')
        os.system('start notepad.exe')
    elif 'close notepad' in command:
        response_text.insert(tk.END, 'Closing Notepad...\n')
        speak('Closing Notepad...')
        os.system('taskkill /f /im notepad.exe')
    elif 'open' in command:
        words = command.split()
        response_text.insert(tk.END, "Opening " + command)
        words.remove("open")
        work = " ".join(words)
        speak("Opening " + command)

        webbrowser.open("https://www." + work + ".com/")
    # elif 'open google' in command:
    #     response_text.insert(tk.END, "Opening Google...\n")
    #     speak("Opening Google...")
    #     webbrowser.open("https://www.google.com/")
    elif 'play music' in command:
        response_text.insert(tk.END, 'Opening music player...\n')
        speak('Opening music player...')
        os.system('start wmplayer.exe')
    elif 'open mail' in command:
        response_text.insert(tk.END, "Opening Gmail...\n")
        speak("Opening Gmail...")
        webbrowser.open("https://mail.google.com/")
    elif 'open whatsapp' in command:
        response_text.insert(tk.END, "Opening WhatsApp...\n")
        speak("Opening WhatsApp...")
        webbrowser.open("https://web.whatsapp.com/")
    elif 'exit' in command:
        response_text.insert(tk.END, "Exiting...\n")
        speak("Thanks for using me. Have a great day!")
        root.destroy()

def listen_command():
    speak(greet())
    while True:
        command = VoiceCommand().lower()
        process_command(command)

# Create GUI
root = tk.Tk()
root.title("Voice Assistant")

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=5)
style.configure('TLabel', font=('Helvetica', 14))

label = ttk.Label(root, text="Voice Assistant", style='TLabel')
label.pack(pady=10)

start_button = ttk.Button(root, text="Start Assistant", style='TButton', command=listen_command)
start_button.pack(pady=20)

response_text = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD)
response_text.pack(padx=20, pady=10)

exit_button = ttk.Button(root, text="Exit", style='TButton', command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
