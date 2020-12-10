#!/usr/bin/python
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import time
import os
from gtts import gTTS
import webbrowser

my_file = "contacts.txt"


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
        # Speech recognition using Google Speech Recognition
        data = ""
        try:
            # Uses the default API key
            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            data = r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
        return data
    
def sendSMS():
    numbers = []
    names = []
    speak("Select acontact by number: ")   
    #my_file = "contacts.txt"
        # open file in read mode
    with open(my_file, 'r') as file_handle:
            # convert file contents into a list
        lines = file_handle.read().splitlines()
        for i, val in enumerate(lines): 
            #split each line and appends name and number to respective list                
            person = val.split(" ", 1)
            names.append(person[0])
            numbers.append(person[1])
            print(i, names[i], numbers[i])
            if(i + 1 >= len(lines)):
                break
                my_file.close()
    data = recordAudio()        
    i = data
    i = int(i)
    dest = numbers[i]
    speak("Record your message")
    data = recordAudio()
    message = data
    speak("Would you like to send " + message + " to " + names[i] + "?")
    data = recordAudio()
    if "yes" in data:
        os.system("kdeconnect-cli --send-sms '%s' -n s20 --destination %s"  % (message, dest))
        speak("Message sent to " + names[i])

        
def jarvis(data):
    if "how are you" in data:
        speak("I am fine, thanks")

    if "what time is it" in data:
        speak(time.strftime("%A %B %d %I:%M %p"))

    if "where is" in data:
        data = data.split(" ", 2)
        location = data[2]
        speak("Hold on Tim, I will show you where " + location + " is.")
        webbrowser.open_new_tab("https://www.google.com/maps/place/" + location + "/&amp;")
        
    if "search for" in data:
        data = data.split(" ", 2)
        search = data[2]
        speak("Hold on Tim, I will search for " + search)
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=' + search)
        
    if "start" in data:
        data = data.split(" ", 1)
        start = data[1]
        start = start.lower()
        speak("Starting " + start)
        os.system(start + "&")
        
    if "signal" in data:
        os.system("signal-desktop &")
        
    if "hey Jane" in data:
        speak("Hey Tim, what's up?")
        
    if "send text" in data:
        sendSMS()
        
    if "open Instagram" in data:
        instagram = 'istekram'
        os.system(istekram + "&")
    
# initialization
time.sleep(.5)
speak("Hi Tim, how can I help?")
while 1:
    data = recordAudio()
    jarvis(data)

            #split each line and appends name and number to respective list                
            person = val.split(" ", 1)
            names.append(person[0])
            numbers.append(person[1])
            print(i, names[i], numbers[i])
            if(i + 1 >= len(lines)):
                break
    speak("Select acontact by number: ")
    data = recordAudio()        
    i = data
    i = int(i)
    dest = numbers[i]
    speak("Record your message")
    data = recordAudio()
    message = data
    speak("Would you like to send " + message + " to " + names[i] + "?")
    data = recordAudio()
    if "yes" in data:
        os.system("kdeconnect-cli --send-sms '%s' -n s20 --destination %s"  % (message, dest))
        speak("Message sent to " + names[i])

def jarvis(data):
    if "how are you" in data:
        speak("I am fine, thanks")

    if "what time is it" in data:
        print(ctime())
        #speak(ctime())

    if "where is" in data:
        data = data.split(" ", 2)
        location = data[2]
        speak("Hold on Tim, I will show you where " + location + " is.")
        webbrowser.open_new_tab("https://www.google.com/maps/place/" + location + "/&amp;")
        
    if "search for" in data:
        data = data.split(" ", 2)
        search = data[2]
        speak("Hold on Tim, I will search for " + search)
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=' + search)
        
    if "start" in data:
        data = data.split(" ", 1)
        start = data[1]
        start = start.lower()
        speak("Starting " + start)
        os.system(start + "&")
        
    if "signal" in data:
        os.system("signal-desktop &")
        
    if "hey Jane" in data:
        speak("Hey Tim, what's up?")
        
    if "send text" in data:
        sendSMS()
        
    if "open Instagram" in data:
        instagram = 'istekram'
        os.system(istekram + "&")
    
# initialization
time.sleep(.5)
speak("Hi Tim, how can I help?")
while 1:
    data = recordAudio()
    jarvis(data)
