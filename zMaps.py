import googlemaps as gm
import urllib.request
import nltk
from bs4 import BeautifulSoup
import json
import httplib2 as http

'''gmaps = gm.GoogleMaps("AIzaSyCFn2iAaiYLCYRmCE4zInueGfuiDsG8weU")
print("Enter the exact adress you wish to go to, speak clearly")
speak.speak("Enter the exact address you wish to go to, speak clearly, though if its a general location, like a road, ignore the numeric adress, and ignore the singapore locator")
with sr.Microphone as source:
    destination = r.listen(source)
    destination = str(r.recognize_google(destination))
    print("Your destination is: "+destination)
    speak.speak("Your destination is: "+destination)

print("Enter the exact adress you are at, speak clearly")
speak.speak("Enter the exact address you are at, speak clearly")
with sr.Microphone as source:
    origin = r.listen(source)
    origin = str(r.recognize_google(origin))
    print("Your destination is: "+origin)
    speak.speak("Your destination is: "+origin)
origin1 = nltk.word_tokenize(origin)
destination1 = nltk.word_tokenize(destination)'''
origin1 = ["Holland", "Road"]
destination1 = ["Buona", "Vista", "Rd"]

temp = []

for i in origin1:
    temp.append(i)
    temp.append('+')
del temp[-1]
origin1 = temp[:]
temp = []
for i in destination1:
    temp.append(i)
    temp.append('+')
del temp[-1]
destination1 = temp[:]
origin1 = "".join(origin1)
destination1 = "".join(destination1)
print(origin1)

h = http.Http()
thing = 'https://maps.googleapis.com/maps/api/directions/json?origin='+origin1+'&destination='+destination1+'&mode=Walking&key=AIzaSyCFn2iAaiYLCYRmCE4zInueGfuiDsG8weU'
response, content = h.request(thing)
jsonObj = json.loads(content)
response = dict(jsonObj)
print(
response["routes"][0]["legs"][0]["start_address"])
for i in range(len(response["routes"][0]["legs"][0]["steps"])):
    print(BeautifulSoup(response["routes"][0]["legs"][0]["steps"][i]["html_instructions"]), "html.parser").get_text()
'''for i in len(response["routes"]["0"]["Steps"]):
    response = response["routes"]["0"]["Steps"][i]["html_instructions"]
    print(BeautifulSoup(response).get_text())
    response = urllib.request.urlopen(thing).read()'''