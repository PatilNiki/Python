import os
import pyttsx3
# import webbrowser

pyttsx3.speak("Welcome!!")
pyttsx3.speak("What should I do for you?")

while(True):
    pyttsx3.speak("Enter a request")
    request = input("Enter a request: ")
    # print(request)

    if((("open" in request) or ("run" in request) or ("start" in request)) and (("chrome" in request) or ("firefox" in request) or ("web" in request) or ("browser" in request) or ("internet" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening browser!!")
        # Checks the installed browser and opens one of them
        if(os.system("start chrome.exe") == 0):
            pass
        elif(os.system("start firefox.exe") == 0):
            pass
        elif(os.system("start msedge.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "No browsers found! Please check if you have any browser installed")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("notepad" in request) or ("text" in request) or ("editor" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening notepad!!")
        os.system("start notepad.exe")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("player" in request) or ("video" in request) or ("media" in request) or ("mp4" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening media player!!")
        if(os.system("start vlc.exe") == 0):
            pass
        elif(os.system("start wmplayer.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "No media players found! Please check if you have any installed")

    elif((("play" in request) or ("start" in request) or ("start" in request)) and (("music" in request) or ("mp3" in request) or ("song" in request) or ("audio" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Launching Music Player!!")
        os.system("start mswindowsmusic:")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("pdf" in request) or ("adobe" in request) or ("acrobat" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening Adobe pdf reader!!")
        if(os.system("start AcroRd32.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "No pdf readers found! Please check if you have any installed")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("GitHubDesktop" in request) or ("GitHub" in request) or ("Git" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening GitHub Desktop!!")
        if(os.system("start GitHubDesktop.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "GitHub Desktop not found! Please check if you have it installed")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("visual" in request) or ("vs" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening visual studio!! Happy Coding")
        if(os.system("start devenv.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "Visual Studio not found! Please check if you have it installed")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("vscode" in request) or ("editor" in request) or ("code" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening your favourite Code Editor!! Happy Coding")
        if(os.system("start Code") == 0):
            pass
        elif(os.system("start notepad++.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "No code editors found! Please check if you have any installed")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("studio64" in request) or ("android" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening Android studio!!")
        if(os.system("start studio64.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "Android Studio not found! Please check if you have any installed")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("blender" in request) or ("3d" in request) or ("design" in request) or ("animation" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening Blender!!")
        if(os.system("start blender.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "Blender not found! Please check if you have any installed")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("Unity" in request) or ("game" in request) or ("aug" in request) or ("game" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening Unity!!")
        if(os.system("start Unity.exe") == 0):
            pass
        else:
            pyttsx3.speak(
                "Unity was not found! Please check if you have any installed")

    elif((("open" in request) or ("run" in request) or ("start" in request)) and (("mspaint" in request) or ("paint" in request) or ("draw" in request) or ("sketch" in request)) and (("don't" not in request) or ("do not" not in request))):
        pyttsx3.speak("Opening microsoft paint!!")
        os.system("start mspaint")

    elif(("stop" in request) or ("end" in request) or ("finish" in request) or ("close" in request)):
        pyttsx3.speak("closing program!!")
        pyttsx3.speak("Thank You")
        break
