#Hackerzzz
# team of 4 members

#REVA UNIVERSITY
#SCHOOL OF EEE

#Divya Srivastava
#Wali Haider
#Sanjay Panda j
#Preety s kotigaudar


import datetime
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import time as tt


name_list=['sanjay','wali','divya''likhith','mom']
no_list=["+916360334188","+916394862429","+917309570109","+919900697723","+919900762506"]


listener= sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)
engine.setProperty("rate",140)
print('Hello sir my name is TARS ,what can i do for you?')
engine.say('Hello sir my name is TARS ,what can i do for you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.5
            audio = r.listen(source)

        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in')
            print(f"User told : {command}\n")


        except Exception as e:

            print("Can you repeat it please")
            talk("Can you repeat it please")
            return "None"
        return command



def run_tars():
        command = take_command()
        command=command.lower()
        command = command.replace('tars', '')
        print(command)

        if 'play' in command:
            video = command.replace('play', '')
            talk('playing')
            pywhatkit.playonyt(video)

        elif 'google' in command:
            info = command.replace('google', '')
            info = command.replace('who is','')
            talk('searching'+info)
            pywhatkit.search(info)
            print('Searching...')


        elif 'whatsapp' in command:
            info = command.replace('whatsapp', '')
            try:
                talk('Whom are you missing?')
                print('Whom are you missing?')
                name=take_command()
                name=name.lower()
                for i in name_list:
                    if i in name:
                        number=no_list[name_list.index(i)]

                print(number)
                talk('Message Please')
                info = take_command()
                pywhatkit.sendwhatmsg_instantly(number,info)
                print('Sent successfully')
                pywhatkit.show_history()
            except:
                print('An unsuccessful error occurred!')



        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('current time is' +time)
            print(time)


        elif 'tell me about' in command:
            thing1 = command.replace('tell me about', '')
            info = wikipedia.summary(thing1, 1)
            print(info)
            talk(info)


        elif 'are you single' in command:
            talk('yes , i was waiting for you to ask me on a date')
        elif 'good morning' in command:
            talk(' very good morning')
        elif 'good afternoon' in command:
            talk('good afternoon')
        elif 'good evening' in command:
            talk('happy evening')
        elif 'good night' in command:
            talk('good night,sweet dreams')
        elif 'thank you' in command:
            talk('ok.......ba bye')
            tt.sleep(3600)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif'who am i' in command:
            talk('if you talk then definitely ,you are a human!')

        elif 'shut up ' in command:
            talk('okay ill be back in a few seconds')
            tt.sleep(15)

        elif 'shutdown' in command:
            talk('Thanks for giving me your time')
            pywhatkit.shutdown(100)
        elif 'cancel shutdown' in command:
            pywhatkit.cancel_shutdown()


        else:
            talk('Sorry ,I did not understand')


while True:
    run_tars()










