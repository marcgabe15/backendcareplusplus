import time
import requests
from matrix_lite import gpio
from meteocalc import Temp, dew_point, heat_index
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

# def humidityReadout():
# 	humidity = sensors.humidity.read().humidity
# 	print(humidity)
#
# 	humidityLED = int((humidity / 100) * 35)
#
# 	if (humidityLED > 34):
# 		humidityLED = humidityLED / 2
# 		brightness = 2
# 	else:
# 		brightness = 1
# 	ledSet = []
#
# 	for x in range(1, int(humidityLED)):
# 		ledSet.append((0,0,25 * brightness,0))
# 		led.set(ledSet)
# 		time.sleep(0.1)
#
# 	time.sleep(5)

def humidityReadout():
	humidity = sensors.humidity.read().humidity
	print(humidity)
	color = [0,50,255,0]

	humidityLED = int((humidity / 100) * 35)
	removeLED = 35 - humidityLED
	print('remove ' + str(removeLED))
	led_list = fade_in([0,50,255,0])
	print(led_list)
	p = 0
	n = 34

	while removeLED > 0:
		if removeLED > 0:
			led_list[p] = 'black'
			led.set(led_list)
			p += 1
			removeLED -= 1
			time.sleep(0.05)

		if removeLED > 0:
			led_list[n] = 'black'
			led.set(led_list)
			n -= 1
			removeLED -= 1
			time.sleep(0.05)

	time.sleep(4)
	removeLED = humidityLED

	while removeLED > 0:
		if removeLED > 0:
			led_list[p] = 'black'
			led.set(led_list)
			p += 1
			removeLED -= 1
			time.sleep(0.05)

		if removeLED > 0:
			led_list[n] = 'black'
			led.set(led_list)
			n -= 1
			removeLED -= 1
			time.sleep(0.05)

def heatIndex():
	temperatureHI = (sensors.pressure.read().temperature) - 5
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

# def heatIndex():
# 	temperatureHI = (sensors.pressure.read().temperature) - 5
# 	humidityHI = sensors.humidity.read().humidity
# 	hi = heat_index(temperature=temperatureHI, humidity= humidityHI)
# 	min_hi = 0
# 	max_hi = 30

def phoneContact():
	url = 'https://maker.ifttt.com/trigger/call/with/key/br6w0TeQJiNDHpWuKYInm6'
	x = requests.post(url, data = 'test')
	print("Reached")

def dangerAlert():
	while True:
		led.set('Red')
		time.sleep(.10)
		led.set('Black')
		time.sleep(.10)

def array_gen(color):
	array = []
	for n in range(35):
		array.append(color)
	return array


def fade_in(max_color):
	led.set('black')
	color = [0,0,0,0]
	min_color = [0,0,0,0]
	terminate = [0,0,0,0]
	delay = 0.0015

	while terminate != [1,1,1,1]:
		for n in range(4):
			if color[n] < max_color[n]:
				color[n] += (max_color[n]/255)
			else:
				terminate[n] = 1
		led.set((color[0],color[1],color[2],color[3]))
		print(color)
		time.sleep(delay)
	return array_gen(color)

def fade_out(max_color):
	led.set('black')
	min_color = [0,0,0,0]
	terminate = [0,0,0,0]
	terminate = [0,0,0,0]
	while terminate != [1,1,1,1]:
		for n in range(4):
			if color[n] > min_color[n]:
				color[n] -= (max_color[n]/255)
			else:
				terminate[n] = 1
		led.set((color[0],color[1],color[2],color[3]))
		print(color)
		time.sleep(.002)

gpio.setFunction(0, 'DIGITAL')
gpio.setMode(0, "input")

while True:
	led.set('Black')
	temperatureReadout(0)
	humidityReadout()
	heatIndex()
	led.set('Black')
