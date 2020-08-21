import pyttsx3
import os

pyttsx3.speak("Welcome!!")
pyttsx3.speak("What should I do for you?")

while(True):
    pyttsx3.speak("Enter a request")
    request=input("Enter a request: ")
    #print(request)
    
    if((("open" in request) or ("run" in request) or ("start" in request)) and (("chrome" in request) or ("browser" in request) or ("internet" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening chrome!!")
        os.system("chrome")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("notepad" in request) or("text" in request) or ("editor" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening notepad!!")
        os.system("notepad")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("player" in request) or("video" in request) or ("media" in request) or ("mp4" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening windows media player!!")
        os.system("wmplayer")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("pdf" in request) or("adobe" in request) or ("acrobat" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening Adobe pdf reader!!")
        os.system("AcroRd32")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("GitHubDesktop" in request) or("GitHub" in request) or ("Git" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening GitHub Desktop!!")
        os.system("GitHubDesktop")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("visual" in request) or("vs 2010" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening visual studio 2010!!")
        os.system("devenv")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("studio64" in request) or("android" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening Android studio!!")
        os.system("studio64")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("blender" in request) or("3d" in request) or("design" in request) or("animation" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening Blender!!")
        os.system("blender")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("Unity" in request) or("game" in request) or("aug" in request) or("game" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening Unity!!")
        os.system("Unity")
    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("mspaint" in request) or("paint" in request) or("draw" in request) or("sketch" in request)) and (("don't" not in request) or("do not" not in request))):
        pyttsx3.speak("Opening microsoft paint!!")
        os.system("mspaint")
    elif(("stop" in request) or ("end" in request) or ("finish" in request) or ("close" in request)):
        pyttsx3.speak("closing program!!")
        pyttsx3.speak("Thank You")
        break;
    else:
        pyttsx3.speak("invalid request!!")
        print("Invalid request!!")

