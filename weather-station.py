import time
import datetime
import requests
import json
from matrix_lite import gpio
from meteocalc import Temp, dew_point, heat_index
from matrix_lite import led
from matrix_lite import sensors
	
def temperatureReadout(override):
	temperature = sensors.pressure.read().temperature
	print(temperature)

	temperatureLED = temperature - 10

	if (override > 0):
		temperatureLED = override

	ledSet = []

	for x in range(1, int(temperatureLED)):
		ledSet.append((25,0,0,0))
		led.set(ledSet)
		time.sleep(0.1)

	led.set(ledSet)

	if(temperatureLED > 40):
		phoneContact()
		led.set('White')
		dangerAlert()

	time.sleep(5)

def humidityReadout():
	humidity = sensors.humidity.read().humidity
	print(humidity)

	humidityLED = int((humidity / 100) * 35)

	if (humidityLED > 34):
		humidityLED = humidityLED / 2
		brightness = 2
	else:
		brightness = 1
	ledSet = []

	for x in range(1, int(humidityLED)):
		ledSet.append((0,0,25 * brightness,0))
		led.set(ledSet)
		time.sleep(0.1)

	time.sleep(5)
	
def heatIndex():
	temperatureHI = (sensors.pressure.read().temperature) - 8
	humidityHI = sensors.humidity.read().humidity
	hi = heat_index(temperature=temperatureHI, humidity= humidityHI)

	ledSet = []

	for x in range(1, int(hi)):
		ledSet.append((25,0,25,0))
		led.set(ledSet)
		time.sleep(0.1)

	if (int(hi) >= 40):
		phoneContact()
		dangerAlert()

	print(hi)
	time.sleep(5)

def phoneContact():
	url = 'https://maker.ifttt.com/trigger/call/with/key/br6w0TeQJiNDHpWuKYInm6'
	x = requests.post(url, data = 'test')
	print("Reached")

def dangerAlert():
	while True:
		led.set('Red')
		time.sleep(.5)
		led.set('Black')
		time.sleep(.5)

def sendWeatherData():
	humidity = sensors.humidity.read().humidity
	temperature = sensors.pressure.read().temperature - 8
	hi = heat_index(temperature=temperature, humidity= humidity)
	uri = "https://shellhacks2019-1f061.appspot.com/addMarker"
	x = requests.post(uri, json = {'humid' : int(humidity), 'heatindex' : int(hi), 'bodytext' : 'SOS', 'fallenAlert' : 'false', 'temp' : int(temperature)})
	print(x)

gpio.setFunction(0, 'DIGITAL')
gpio.setMode(0, "input")

while True:
	currentDT = datetime.datetime.now()
	led.set('Black')
	temperatureReadout(0)
	humidityReadout()
	heatIndex()

	if (currentDT.minute % 6 == 0):
		sendWeatherData()

	led.set('Black')
	
