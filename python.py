import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki

listener = sr.Recognizer()
speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', 150)


def speak(text):
    speaker.say('yes, ' + text)
    speaker.runAndWait()


def speak_exit(text):
    speaker.say(text)
    speaker.runAndWait()


va_name = "sneha"
speak_exit('I am your ' + va_name + ", tell me.")


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Listening.........")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + ' ', '')

    except:
        print("check your microphone")
    return command


while True:
    user_command = take_command()
    if 'close' in user_command:
        print("see you again.i will be there for you whenever you call me.")
        speak("see you again.i will be there for you whenever you call me.")
        break
    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)
    elif 'play' in user_command:
        user_command = user_command.replace('play ', '')
        print('Playing ' + user_command)
        speak('Playing ' + user_command + ", enjoy.")
        pk.playonyt(user_command)
        break
    elif 'search for' in user_command or 'google for' in user_command:
        user_command = user_command.replace('search for ', '')
        user_command = user_command.replace('google for ', '')
        speak('Searching for ' + user_command)
        pk.search(user_command)
        break
    elif 'who is' in user_command:
        user_command = user_command.replace('who is ', '')
        info = wiki.summary(user_command, 3)
        print(info)
        speak(info)
        break
    elif 'who are you' in user_command:
        speak_exit('I am your virtual voice assistant,tell me.')
    else:
        speak_exit("Please Say it Again.")

