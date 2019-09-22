import time
import requests
import asyncio
import websockets
import json
import pprint
from meteocalc import Temp, dew_point, heat_index
from matrix_lite import led
from matrix_lite import sensors

def detectFall():
    data = sensors.imu.read()
    print(data.accel_x)
    print(data.accel_y)
    print(data.accel_z)
    print ("--------------------")

    if (abs(data.accel_x) > 1.70 and abs(data.accel_x) < 10):
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
    humidity = sensors.humidity.read().humidity
    temperature = sensors.pressure.read().temperature - 8
    hi = heat_index(temperature=temperature, humidity= humidity)
    uri = "https://shellhacks2019-1f061.appspot.com/addMarker"
    x = requests.post(uri, json = {'humid' : int(humidity), 'heatindex' : int(hi), 'bodytext' : 'SOS', 'fallenAlert' : 'true', 'temp' : int(temperature)})
    print(x)
    

def phoneContact():
	url = 'https://maker.ifttt.com/trigger/temp/with/key/br6w0TeQJiNDHpWuKYInm6'
	#x = requests.post(url, data = 'test')
	print("Reached")

while True:
    led.set('Black')
    detectFall()
