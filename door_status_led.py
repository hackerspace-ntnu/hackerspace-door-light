# By Geir Kulia, 28. August 2014

# Set up GPIO for LED
import RPi.GPIO as GPIO
import time, urllib2, json

pin_number_LED = 7
api_host = "http://hackerspace.idi.ntnu.no/api/door"

def main():
	GPIO.setup(pin_number_LED, GPIO.OUT)

	while True:
	# check if internet is connected
	if internet_on():
		# Write to GPIO
		if checkDoor():
			setLED(True)
		else:
			setLED(False)

		time.sleep(10) # Delay 10 second
	else:
		# Blink if no connection
		setLED(False)

def setLED(value):
	GPIO.output(pin_number_LED, value)
     
def internet_on():
	# check connection 
    try:
        response=urllib2.urlopen(api_host, timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

def checkDoor():
	# Check if the door is open
	response = urllib2.urlopen(api_host)
	data = json.loads(response.read())

	return data[0]['isOpen']

if __name__ == "__main__":
	main()

