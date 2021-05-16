import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition == speech from microphone to text
import smtplib
# from secrect import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui #pip install pyautogui
import webbrowser as wb
from time import sleep
import wikipedia #pip install wikepedia
import pywhatkit 
import requests
# from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt 
import string
import random
import psutil
from nltk.tokenize import word_tokenize
import wolframalpha
import pandas as pd 
import subprocess


  
 

try:
    client = wolframalpha.Client("<YOUR API KEY>")
except Exception:
    speak("Please connect to the internet Sir!")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def getvoices(voice):
#     voices = engine.getProperty('voices')
#     # print(voices[1].id)
#     if voice == 1:
#         engine.setProperty('voice', voices[0].id)
#         speak('Hello! This is Jarvis')
#     if voice == 2:
#         engine.setProperty('voice', voices[1].id)
#         speak('Hello! This is Friday')

    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # Hour = I Minutes = M Seconds  = S
    speak("The current time is:")
    speak(Time)
    
     

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is: ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    # speak("Welcome back Sir! All Systems for gaming will be prepared in a few minutes. For now feel free to grab a cup of coffe and have a good day")
    time()
    date()
    speak("At your service Sir!")
    
  #PLease check how to use PYAUTOGUI if you dont know from this url - https://youtu.be/V3IOfvGmqxs

def sign_in(meetingid, pswd):
    subprocess.call(["C:/Users/Admin/AppData/Roaming/Zoom/bin/Zoom.exe"])
    sleep(5)
    # Clicks the join button
    join_btn =pyautogui.locateCenterOnScreen('join_btn.png') 
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    sleep(3)
    # Type the meeting id
    meeting_id_btn =pyautogui.locateCenterOnScreen('enterMeetingID.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.write(meetingid)
    # Click Join Meeting
    joinBtn = pyautogui.locateCenterOnScreen('join.png')
    pyautogui.moveTo(joinBtn)
    pyautogui.click()
    sleep(5)
    # Type the meeting pass
    meeting_pass_btn =pyautogui.locateCenterOnScreen('enterPass.png')
    pyautogui.moveTo(meeting_pass_btn)
    pyautogui.write(pswd)
    #  Clicks the joinMeeting 
    join_btn =pyautogui.locateCenterOnScreen('joinMeeting.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    


def greeting():
    hour = datetime.datetime.now().hour
    
    if hour >= 6 and hour <12:
        speak("Good Morning Sir"
    elif hour >= 12 and hour <18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour <24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir!")
    

# while True:
#     voice = int(input('Press 1 for Male voice\nPress 2 for Female voice'))
#       speak(audio)
#      getvoices(voice)
#      wishme()
#      greeting()

def takeCommandCmd():
    query = input("please tell me how can i help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-in")
        print(query)
    except Exception as e:
        print(e)   
        print("Say that again please....")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mailID', 'passwd')
    server.sendmail('mailID', to, content)
    server.close()

def sendWhatsappMsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(8)
    pyautogui.press('enter')

def searchgoogle():
    speak("What Should I search?")
    search = takeCommandMic()
    speak("Searching Google...")
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key='<API KEY>')
    speak("What Topic should I search for Sir?")
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                    language='en',
                                    page_size=5)
    
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')

    speak("That's it for now I'll update you in some time")

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.jason()
    covid_data = f'Confirmed cases : {data["cases"]} \n Deaths : {data["deaths"]} \n Recovered : {data["recovered"]}'
    print(covid_data)
    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'G:\\JARVIS\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def passwordGen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    passlen = 8
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("Okay Sir, flipping a coin")
    coin = ['heads', 'tails']
    toss=[]
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("I flipped a coin Sir! and you got"+toss)

def roll():
    speak("Ok Sir Rolling a Die for you")
    die = ['1','2','3','4','5','6']
    roll=[]
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("Sir I rolled a die and you got "+roll)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at '+usage)
    battery = psutil.sensors_battery()
    speak("Sir is battery is currently at ")
    speak(battery.percent)


if __name__ == "__main__":
    speak("Hello I am Jarvis")
    # getvoices(1)
    # wishme()
    greeting()
    # wakeword = "jarvis"
    while True:
        query = takeCommandMic().lower()
        # query = word_tokenize(query)
        print(query)
        # if wakeword in query:
        if 'time' in query:
                time()
            
        elif 'date' in query:
                date()
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommandMic()
                to = "laharupam71@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")   

        elif 'message' in query:
            user_name = {
                'FRIEND' : '+91 1234567890',
                'father' : '+91 1234567890',
                'mother' : '+91 1234567890',
                
                }
            try:
                speak("Whom should I message")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("What should I send?")
                message = takeCommandMic()
                sendWhatsappMsg(phone_no, message)
                speak("Message has been sent!")
                        
            except Exception as e:
                print(e)
                speak("Sorry I was unable to send the message")
            
        elif 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query.replace("wikipedia","")
            query.replace("jarvis","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

       
 
        elif 'temperature in kolkata' in query:
              
            # Use the same API key  
            # that we have generated earlier 
            client = wolframalpha.Client("api key") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results")

        elif 'search' in query:
            searchgoogle()
        
        elif 'coders paradise' in query:
            speak("Sir I am connecting you to stackoverflow.")
            wb.open('https://stackoverflow.com')
                
        elif 'youtube' in query:
            speak("What should I play?")
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)

                
                
        elif 'weather' in query: 
            city = 'new york' 
            url='https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=816bcbf9a9b7eea594e91662191115ca'

            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp = data['weather'] [0] ['description']
            temp = round((temp - 32)*5/9)
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} city is like')
            speak('Temperature : {} degree celcius'.format(temp))
            speak('weather is {}'.format(desp))

        elif 'news' in query:
            news()

        elif 'read' in query:
            text2speech()

        elif 'covid' in query:
            covid()

        elif 'open code' in  query:
            codepath = 'path-of-application'
            os.startfile(codepath)

        elif 'documents' in query:
            codepath = 'path-of-application'
            os.startfile(codepath)
     
        elif 'joke' in query:
                speak(pyjokes.get_joke())
                
        elif 'screenshot' in query:
                screenshot()

        elif 'remember' in query:
            speak("What should I remember?")
            data = takeCommandMic()
            speak("Ok Sir! You told me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close() 

        elif 'anything' in query:
            remember = open('data.txt', 'r')
            speak("You told me to remember that "+remember.read())
                
        elif 'password' in query:
            passwordGen()

        elif 'flip' in query:
            flip()
        
        
        
        elif 'keep it up' in query:
            speak("Nis  choey sir")

        elif 'roll' in query:
            roll()

        elif 'cpu' in  query:
            cpu()

        elif 'offline' in query:
            speak("Have a good day Sir!")
            quit()

        elif 'thanks' in query:
            speak("No problem sir")

        elif 'word' in query:
            codepath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(codepath)

        elif 'photoshop' in query:
            codepath='C:\\Program Files\\Adobe\\Adobe Photoshop 2021\\Photoshop.exe'
            os.startfile(codepath)

        elif 'zoom' in query:
            sign_in('meeting id', 'password')

        elif 'play music' in query:
            codepath='<ENTER MUSIC PATH>'
            os.startfile(codepath)
            
        elif 'geography' in query:
            try:
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                speak("Connection Error!")   
        elif 'check your system' in query:
            speak("Yes Sir checking my system")
            speak("Initializing test 1")
            speak("Test 1 successfull")
            speak("Initializing test 2")
            speak("Test 2 successfull")
            speak("Initializing test 3")
            speak("Test 3 successfull")
            speak("All systems are working fine sir!")

        elif 'close code' in query:
            speak("Ok Sir closing code and turning off JARVIS")
            sleep(3)
            os.system("taskkill/im Code.exe")
        
        
          

            

# takeCommandMic == "hey jarvis " tokenize = ['hey' , 'jarvis']
