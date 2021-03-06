import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import random


#listening side
listener = sr.Recognizer()

#speaker / voice
engine = pyttsx3.init()
#setting up the voice 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#talking function
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ''
    try:
        #using michrophone as source
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            
            #changing the command to lowercase
            command = command.lower()
            
            #checking if alexa key is mentioned, if so to the command
            if 'alex' in command:
                command = command.replace('alex', '')
                print("Command: ",command)
    except:
        pass
    
    return command

userName = 'master'

def run():
    #bc of bugs I changed command to Kommand
    Kommand = take_command()
    global userName
    
    if 'play' in Kommand:
        song = Kommand.replace('play', '')
        talk('Playing' + song)
        print('Playing' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in Kommand:
        time = datetime.datetime.now().strftime('%H:%M')
        print('Current time is ' + time)
        talk('Current time is ' + time)
        
    elif 'who is' in Kommand:
        person = Kommand.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'what is' in Kommand:
        person = Kommand.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'joke' in Kommand:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        
    #open function - adding more sites
    elif 'open' in Kommand:
        site = Kommand.replace('open', '')
        print('Opening ' + site)
        talk('Opening ' + site)
        if 'google' in site:
            url = "https://www.google.com/"
            webbrowser.open(url, new=0, autoraise=True)
        elif 'youtube' in site:
            url = "https://www.youtube.com/"
            webbrowser.open(url, new=0, autoraise=True)
    #have a client name and functions to it 
    
    elif 'roll the dice' in Kommand:
        first_choice = random.randint(1,6)
        second_choice = random.randint(1,6)
        print('First choice:' + str(first_choice) + "\nSecond choice:"+ str(second_choice))
        talk('First choice:' + str(first_choice) + "\nSecond choice:"+ str(second_choice))
        
    elif 'call me' in Kommand:
        name = Kommand.replace('call me', '')
        userName = name;
        print('From now on I will call you ' + userName)
        talk('From now on I will call you ' + userName)
        
    elif "what's my name" in Kommand:
        print('Your name is ' + userName)
        talk('Your name is ' + userName)
        
    
    elif 'exit' in Kommand:
        print('Exiting...')
        talk('Exiting...')
        quit()
            
    else:
        print('Please say the command again.')
        talk('Please say the command again.')

while True:
    run()