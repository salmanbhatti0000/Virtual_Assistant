import speech_recognition as sr
import webbrowser
import pyttsx3
import requests



recognizer = sr.Recognizer()
import pywhatkit

def play_youtube_song(song):
    pywhatkit.playonyt(song)


def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    """Process website commands or fetch AI-generated answers."""
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "play" in c.lower():
        song = c.replace("play", "").strip()
        play_youtube_song(song)
        speak(f"Playing {song} on YouTube.")
   
    else:
        print(c)


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
