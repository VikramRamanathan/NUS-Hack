import json
from urllib.parse import urlparse
import httplib2 as http
def BusTime(busstopcode, busno):
    if __name__ == "__main__" or __name__ == "BusTest":
        headers = { 'AccountKey': 'qmWBViobQ86zp60c7OrjxA==', 'accept': 'application/json'}
        uri = 'http://datamall2.mytransport.sg/'
        path = '/ltaodataservice/BusArrivalv2?BusStopCode=' + busstopcode
        target = urlparse(uri + path)
        print (target.geturl())
        method = 'GET'
        body = ''
        h = http.Http()
        response, content = h.request(target.geturl(), method, body, headers)
        jsonObj = json.loads(content)
        t = dict(jsonObj)
        for i in t['Services']:
            if str(i['ServiceNo']) == busno:
                EstimatedArrival = i["NextBus"]["EstimatedArrival"]
                Load = i["NextBus"]["Load"]
                Feature = i["NextBus"]["Feature"]
                Type = i["NextBus"]["Type"]
                '''print('ServiceNo: ', i['ServiceNo'])
                print("EstimateArrival: ", EstimatedArrival)
                print("Load: ", Load)
                print("Feature: ", Feature)
                print("Type: ", Type)'''
                return EstimatedArrival, Load, Feature, Type