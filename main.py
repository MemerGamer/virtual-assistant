import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

#listening side
listener = sr.Recognizer()

#speaker / voice
engine = pyttsx3.init()
#setting up the voice 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#talking function
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        #using michrophone as source
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            
            #changing the command to lowercase
            command = command.lower()
            
            #checking if alexa key is mentioned, if so to the command
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print("Command: ",command)
    except:
        pass
    return command

def run_alexa():
    #bc of bugs I changed command to Kommand
    Kommand = take_command()
    
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
        person = Kommand.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    elif 'joke' in Kommand:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        print('Please say the command again.')
        talk('Please say the command again.')
while True:
    run_alexa()