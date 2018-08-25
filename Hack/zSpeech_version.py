import speech_recognition as sr
import zBusTest as BusTest
import zTimeScript as TimeScript
import pyglet
pyglet.lib.load_library('avbin64')
pyglet.have_avbin64=True
import time
from gtts import gTTS
import zSpeak as speak

r = sr.Recognizer()

while True:
    print("This is Bus Help version Alpha 0.1")
    speak.speak("This is Bus Help version Alpha 0.1")
    print("Please enter your current bus stop code. Please enter this in the following format. Example: zero zero four eight one")
    speak.speak("Please enter your current bus stop code. Please enter this in the following format. Example: zero zero four eight one")
    with sr.Microphone() as source:
        BSCSTR = str(r.listen(source))
        print("You said: " + BSCSTR)
        speak.speak("You said: " + BSCSTR)
    print("Please enter your bus number")
    speak.speak("Please enter your bus number")
    with sr.Microphone() as source:
        BNSTR = str(r.listen(source))
        print("You said: " + BNSTR)
        speak.speak("You said: " + BNSTR)
    print("Please enter your destination code. If you do not want one, please say No. Please enter this in the following format. Example: zero zero four eight one")
    speak.speak("Please enter your destination code. If you do not want one, please say No. Please enter this in the following format. Example: zero zero four eight one")
    with sr.Microphone() as source:
        DES = str(r.listen(source))
        print("You said: " + DES)
        speak.speak("You said: " + DES)
    print("If any of the above fields are incorrect, please say No now. Otherwise, say yes")
    speak.speak("If any of the above fields are incorrect, please say No now. Otherwise, say yes")
    with sr.Microphone() as source:
        Temp = str(r.listen(source))
        if Temp == "Yes":
            break
        else:
            pass

Arrival, Seating, Wheelchair, Deck = BusTest.BusTime(BSCSTR,BNSTR)

if Seating == "SEA":
    Seating = "Seats are available"
elif Seating == "SDA":
    Seating = "There is standing room only"
elif Seating == "LSD":
    Seating = "There is limited standing room"
if Wheelchair == "WAB":
    Wheelchair = "wheelchair support"
else:
    Wheelchair = "no wheelchair support"
if Deck == "SD":
    Deck = "Single Decker"
elif Deck == "DD":
    Deck = "Double Decker"
elif Deck == "BD":
    Deck = "Bendy"
print("Your selected bus, "+BNSTR+" will arrive in "+str(TimeScript.timestuff(Arrival))+" minutes. "+Seating+" and the bus has "+Wheelchair+". The bus type is "+Deck+".")
speak.speak("Your selected bus, "+BNSTR+" will arrive in "+str(TimeScript.timestuff(Arrival))+" minutes. "+Seating+" and the bus has "+Wheelchair+". The bus type is "+Deck+".")

while True:
    A = int(TimeScript.timestuff(Arrival))
    if A <= 1:
        print("Your bus is almost here, just wait a bit")
        speak.speak("Your bus is almost here, just wait a bit")
        break
    elif A <= 10:
        print("Your bus is", A, "minutes away")
        speak.speak("Your bus is" + str(A) + "minutes away")
        time.sleep(60)
    elif A >= 10:
        print("Your bus is more than 10 minutes away")
        speak.speak("Your bus is more than 10 minutes away")
        time.sleep(150)

Arrival, Seating, Wheelchair, Deck = BusTest.BusTime(DES,BNSTR)

while True:
    A = int(TimeScript.timestuff(Arrival))
    if A <= 1:
        print("You are almost at your destination. Please ready yourself to alight")
        speak.speak("You are almost at your destination. Please ready yourself to alight")
        break
    elif A <= 10:
        print("Your destination is", A, "minutes away")
        speak.speak("Your destination is" + str(A) + "minutes away")
        time.sleep(60)
    elif A >= 10:
        print("Your destination is more than 10 minutes away")
        speak.speak("Your destination is more than 10 minutes away")
        time.sleep(150)