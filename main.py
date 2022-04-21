import speech_recognition as sr 
import pyttsx3
import pywhatkit

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
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        print('Playing' + song)
        pywhatkit.playonyt(song)
        
        
run_alexa()