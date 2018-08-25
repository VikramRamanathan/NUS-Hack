'''import datetime
import math

A = str(datetime.datetime.now())[14:][:-7]
sum = 1
sum = math.factorial(1000000)
B = str(datetime.datetime.now())[14:][:-7]
amin = int(A[:-3])*60+int(A[3:])
bmin = int(B[:-3])*60+int(B[3:])
print(bmin-amin)'''


'''from googlemaps import GoogleMaps

gmaps = GoogleMaps("AIzaSyCFn2iAaiYLCYRmCE4zInueGfuiDsG8weU")
print("Enter the exact adress you wish to go to, speak clearly")
speak.speak("Enter the exact address you wish to go to, speak clearly")
with sr.Microphone as source:
    '''
input = "5 + Five"
temp = []
try:
    for i in input:
        if i in "1234567890":
            temp.append(i)
except:
    pass
print(temp)