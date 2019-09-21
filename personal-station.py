import time
import requests
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
        time.sleep(5)
        data = sensors.imu.read()
        if (abs(data.gyro_x) > 2.5):
            fallDetected()



    time.sleep(0.250)
    
def fallDetected():
    phoneContact()
    while True:
        led.set('Red')
        time.sleep(.5)
        led.set('Black')
        time.sleep(.5)

def phoneContact():
	url = 'https://maker.ifttt.com/trigger/temp/with/key/br6w0TeQJiNDHpWuKYInm6'
	x = requests.post(url, data = 'test')
	print("Reached")

while True:
    led.set('Black')
    detectFall()