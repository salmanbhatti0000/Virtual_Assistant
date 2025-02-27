import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import os
import subprocess

# Initialize speech recognition
recognizer = sr.Recognizer()

def speak(text):
    # """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def play_youtube_song(song):
    # """Plays a song or video on YouTube."""
    pywhatkit.playonyt(song)

def open_application(app_name):
    # """Opens an application dynamically without setting paths."""
    try:
        subprocess.run(["start", app_name], shell=True)
        speak(f"Open {app_name}")
    except Exception as e:
        speak("Sorry, I couldn't open that application.")
        print(f"Error: {e}")

def close_application(app_name):
    # """Closes an application dynamically."""
    try:
        subprocess.run(["taskkill", "/IM", f"{app_name}.exe", "/F"], shell=True)
        speak(f"Close {app_name}")
    except Exception as e:
        speak("Sorry, I couldn't close that application.")
        print(f"Error: {e}")

def system_control(command):
    # """Handles system control commands like shutdown, restart, and volume control."""
    if "shutdown" in command.lower():
        os.system("shutdown /s /t 10")  # Shutdown in 10 seconds
    elif "restart" in command.lower():
        os.system("shutdown /r /t 10")
    elif "increase volume" in command.lower():
        os.system("nircmd.exe changesysvolume 5000")  # Requires NirCmd tool
    elif "mute" in command.lower():
        os.system("nircmd.exe mutesysvolume 1")

def processCommand(c):
    # """Process commands to open apps, websites, or perform system tasks."""
    c = c.lower()
    
    # Open common websites
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    # Play YouTube videos
    elif "play" in c:
        song = c.replace("play", "").strip()
        play_youtube_song(song)
        speak(f"Playing {song} on YouTube.")

    # Open applications dynamically
    elif "open" in c:
        app_name = c.replace("open", "").strip()
        open_application(app_name)

    # Close applications dynamically
    elif "close" in c:
        app_name = c.replace("close", "").strip()
        close_application(app_name)

    # System control
    elif "shutdown" in c or "restart" in c or "increase volume" in c or "mute" in c:
        system_control(c)

    # If command doesn't match any category
    else:
        speak("I don't understand the command.")
        print(f"Unknown Command: {c}")

if __name__ == "__main__":
    speak("Preparing machine....")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)

            word = recognizer.recognize_google(audio)
            print(f"User: {word}")

            if word.lower() == "hello":
                speak("Yes Sir, what is your wish?")
                
                with sr.Microphone() as source:
                    print("What is your wish...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    
                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
