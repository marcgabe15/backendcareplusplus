import time
import requests
import asyncio
import websockets
import json
import pprint
from matrix_lite import led
from matrix_lite import sensors

def detectFall():
    data = sensors.imu.read()
    print(data.accel_x)
    print(data.accel_y)
    print(data.accel_z)
    print ("--------------------")

    if (abs(data.accel_x) > 1.90 and abs(data.accel_x) < 10):
        print("Possible Fall")
        time.sleep(3)
        data = sensors.imu.read()
        if (abs(data.gyro_x) > 2.5):
            sendWebAlert()
            fallDetected()

    time.sleep(0.250)
    
def fallDetected():
    phoneContact()
    while True:
        led.set('Red')
        time.sleep(.5)
        led.set('Black')
        time.sleep(.5)

def sendWebAlert():
    uri = "https://shellhacks2019-1f061.appspot.com/addMarker"
    #async with websockets.connect(uri) as websocket:
    #    await websocket.send(json.dumps([{'temp' : '37.44', 'humidity' : '50.00', 'fall' : 'true', 'hasFlooded' : 'false', 'bodyTest' : 'Can you see clearly now'}]))
    x = requests.post(uri, json = {'humid' : 37.44, 'heatindex' : 50.00, 'bodytext' : 'SOS', 'fallenAlert' : 'false', 'temp' : 100})
    print(x)
    #uri = "https://shellhacks2019-1f061.appspot.com/markers"
    #x = requests.get(uri, data = '')
    #print(x)
    

def phoneContact():
	url = 'https://maker.ifttt.com/trigger/temp/with/key/br6w0TeQJiNDHpWuKYInm6'
	#x = requests.post(url, data = 'test')
	print("Reached")

while True:
    led.set('Black')
    detectFall()
