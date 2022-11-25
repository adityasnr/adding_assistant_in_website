
import pyttsx3

#initialise Text-to-speech engine
engine = pyttsx3.init()

#convert this text to speech

class Assistant:
    def __init__(self):
        pass

    def start(self):
       text = "hello, what is your name?"
       voices = engine.getProperty("voices")
       engine.setProperty("voice" , voices[0].id)
       engine.say(text)
       engine.runAndWait()
       return

    def one(answer):
        text1 = f"hello {answer}"
        engine.say(text1)
        engine.runAndWait()
        return


    
#    i = 0
#    while i < 100:
#       i = i + 1
#       def question(answer):
#           text2 = f"Hello, {answer}, how can I help you"
#           engine.say(text2)
#           engine.runAndWait()
   
           
