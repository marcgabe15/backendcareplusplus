import time
import requests
from matrix_lite import led
from matrix_lite import sensors
	
def temperatureReadout(override):
	temperature = sensors.pressure.read().temperature
	print(temperature)

	temperatureLED = temperature - 7

	if (override > 0):
		temperatureLED = override

	ledSet = []

	for x in range(1, int(temperatureLED)):
		ledSet.append((25,0,0,0))
		led.set(ledSet)
		time.sleep(0.1)

	led.set(ledSet)

	if(temperatureLED > 28):
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


while True:
	led.set('Black')
	temperatureReadout(0)
	humidityReadout()
	led.set('Black')
	
