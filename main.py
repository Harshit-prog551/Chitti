import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime as dt
from plyer import notification
import pyautogui

engine = pyttsx3.init()
engine.setProperty('rate',150)

def speak(command):
    engine.say(command)
    engine.runAndWait()

def command(): #audio to text
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

            try:
                content = r.recognize_google(audio, language = 'en-in')
                print("You said :",content)
            except Exception as e:
                print("Please try again...",e)
        return content

def audioToText():
    while True:
        req = command()
        print(req)

def main():
    while True:
        req = command().lower()
        if 'hello' in req:
            speak("Welcome , How can i help you?")
        elif 'music' in req:
            speak("Now we are playing music")
            song = random.randint(1,5)
            if(song == 1):
                webbrowser.open("https://www.youtube.com/watch?v=TWfzLpR3Q_E&list=RDTWfzLpR3Q_E&index=1&pp=8AUB")
            elif(song == 2):
                webbrowser.open("https://www.youtube.com/watch?v=B21O_RSjUn4&list=RDTWfzLpR3Q_E&index=6&pp=8AUB")
            elif(song == 3):
                webbrowser.open("https://youtu.be/TKSyQDgrYPw")
            elif(song == 4):
                webbrowser.open("https://youtu.be/zEA8F2vcVn0")
            else:
                webbrowser.open("https://youtu.be/xs7tN0A7RC8")
        elif 'time' in req:
            samay = dt.datetime.now().strftime("%H: %M")
            speak("current time is"+str(samay))
        elif 'date' in req:
            taarekh = dt.datetime.now().strftime("%d: %m")
            speak("current date is"+str(taarekh))
        elif 'new task' in req:
            task = req.replace('new task',"") 
            task = task.strip() #used for remove sapces from ahead and back
            if(task != ""):
                speak("Adding task"+task)
                with open ("todo.txt",'a') as file:
                    file.write(task+"\n")
        elif 'delete task' in req:
            task = req.replace("delete task","").strip()
            with open("todo.txt", "r") as file:
                lines = file.readlines()
            with open ("todo.txt","w") as file:
                for line in lines:
                    if line.strip() != task:  
                        file.write(line)
            speak(f"{task} has been deleted")
                    

        elif 'speak task' in req:
            with open ("todo.txt","r") as file:
                speak("To do task's are :"+file.read())
        elif 'show work' in req:
            with open ("todo.txt","r") as file:
                task = file.read()
            notification.notify(
                title = "Today's work",
                message = task
            )
        elif 'open' in req:
            query = req.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        
                


main()

