import pyaudio
import speech_recognition as sr  
import smtplib
import webbrowser
import os

def voice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Somthing");
        audio = r.listen(source)
        print("Times Up...")
    try:
        text = r.recognize_google(audio)
        k = ("{}".format(text))
        return k
    except:
        print("nopee")
      
    
    

command = voice()
from playsound import playsound


print ("the words are "+ command)
if command == "I want to watch p***" or command == "p***" or command == "open p***":
	print("Whoes Porn Do you want")
	name = voice()
	print(name)
	prn = "https://www.pornhub.com/video/search?search="
	print("opening " + name + "porn")
	porn = prn+name
	webbrowser.open_new(porn)
else:
	print("not working")
