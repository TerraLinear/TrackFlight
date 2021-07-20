#David Prosack


import requests
import os, sys
from bs4 import BeautifulSoup
import json
import time
from time import sleep

#to pick a flight go to https://opensky-network.org and pick a Mode S Code
callSign = input("Call sign of flight?")

def callPlane(todayTime, callSign):
    res = requests.get('https://opensky-network.org/api/states/all?time='+todayTime+'&icao24='+callSign)
    txt = res.text
    txtJson = json.loads(txt)   
    altitude = txtJson["states"][0][13]
    lat = txtJson["states"][0][5]
    long = txtJson["states"][0][6]
    return lat, long, altitude

def newFile():
    i = 1
    while i < 100:
        todayTime = str(int(time.time()))
        print(callPlane(todayTime, callSign))
        time.sleep(10)
        i += 1
    
newFile()
