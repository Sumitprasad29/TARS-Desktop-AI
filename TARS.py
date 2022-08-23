import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import random
import os
import pyautogui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from TARSGUI import Ui_TARSUI
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishME():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good Morning!, its {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon!, its {tt} ")
    else:
        speak(f"Good Evening!, its {tt}")
    speak("Hello sir, I am Tars. How may I help you")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        wishME()
        while True:
            self.query = self.takeCommand().lower()

           # logic for executing tasks
            if 'search' in self.query:
                speak('Searching Wikipedia.....')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")

            elif 'open google' in self.query:
                codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                speak("opening google")
                # cm = takecommand().lower()
                os.startfile(codePath)

            elif 'open amazon' in self.query:
                webbrowser.open("amazon.in")

            elif 'open stack over flow' in self.query:
                webbrowser.open("stackoverflow.com")

            elif 'news' in self.query:
                speak("Finding today's top headlines")
                webbrowser.open("google.com/news")

            elif 'play music' in self.query:
                speak("Playing Music")
                music_dir = 'E:\\Ed Sheeran'
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"The time is {strTime}")

            elif 'volume up' in self.query:
                pyautogui.press("volumeup")

            elif 'volume down' in self.query:
                pyautogui.press("volumedown")

            elif 'mute' in self.query:
                pyautogui.press("volumemute")

            elif "unmute" in self.query:
                pyautogui.press("volumeunmute")

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "you can sleep" in self.query:
                speak("thanks for using me sir, have a good day")
                sys.exit()

    def takeCommand(self):
        # it takes microphone input form the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please......")
            return "None"
        return query


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TARSUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            "E:\TARS AI\Intro-HELLO-FUTURE-1920x1080_v2.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        # label_time = current_time.toString('hh:mm:ss')
        # label_date = current_date.toString(Qt.ISODate)
        # self.ui.textBrowser.setText(label_date)
        # self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
TARS = Main()
TARS.show()
exit(app.exec_())
