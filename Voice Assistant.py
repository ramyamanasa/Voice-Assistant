import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
        
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
        
    else:
        speak("Good evening!")
          
    speak("Hope you are doing well.  I am your AI. Please tell me how may I help you") 
    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'my name' in query:
            speak('Your name is Aiswaryaa Rajesh')

        elif 'my age' in query:
            birth_year = int(2003)
            birth_month = int(2)
            birth_day = int(21)
 
            current_year = datetime.date.today().year
            current_month = datetime.date.today().month
            current_day = datetime.date.today().day
 
            age_year = current_year - birth_year
            age_month = abs(current_month-birth_month)
            age_day = abs(current_day-birth_day)

            age = age_year, age_month, age_day
            print(f"Your age is: {age_year} years {age_month} months {age_day} days")
            speak(f"Your age is: {age_year} years {age_month} months {age_day} days")
        
        elif 'live' in query:
            speak("Delhi")


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            print('opening youtube')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('opening google')
            print('opening google')
            webbrowser.open('google.com') 


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        
        elif 'open command prompt' in query:
            speak('opening command promt')
            print('opening command prompt')
            os.system("start cmd")

       
        elif "that's it" in query:
            speak('Thank you. Call me whenever you need help')
            break
