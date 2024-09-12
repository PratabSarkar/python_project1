import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime
import pyjokes
import os  
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand...") 

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 180)
    engine.say(x)
    engine.runAndWait()

# speechtx("Hello sir, I am jarvis")

if __name__ == "__main__":

    if "hey jarvis" in sptext().lower(): 
            while True:
                    data1=sptext().lower()

                    if "what is your name" in data1:
                        name = "my name is jarvis"
                        print (name)
                        speechtx(name)

                    elif "how old are you" in data1:
                        age = "i am 2 years old"
                        print(age)
                        speechtx(age) 

                    elif "now time" in data1:
                        time = datetime.datetime.now().strftime("%I%M%p")
                        print(time)
                        speechtx(time)

                    elif "open youtube" in data1:
                        webbrowser.open("https://www.youtube.com/")

                    elif "open my youtube channel" in data1:
                         webbrowser.open("https://www.youtube.com/@itzpratab7232")

                    elif "open joke" in data1:
                        joke_1 = pyjokes.get_joke(language="en",category="all")
                        print (joke_1)
                        speechtx(joke_1)

                    elif "play song" in data1:
                        add = "D:\song"
                        listsong = os.listdir(add)
                        print(listsong)
                        os.startfile(os.path.join(add,listsong[0]))

                    elif "exit" in data1:
                        speechtx("thank you")
                        break

                    time.sleep(5)

    else:
        print("Thanks ")




