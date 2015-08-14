# By Geir Kulia, 28. August 2014

import time
import json
import urllib2

import RPi.GPIO as GPIO


SLEEP = 10

LED_PIN = 7
API_HOST = "http://hackerspace.idi.ntnu.no/api/door"


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)

    while True:
        if is_internet_on():
            if is_door_open():
                led_on()
            else:
                led_off()

            time.sleep(SLEEP)
        else:
            # Blink if no connection
            for _ in range(max(1, SLEEP / 2)):
                led_on()
                time.sleep(1)
                led_off()
                time.sleep(1)


def led_on():
    GPIO.output(LED_PIN, True)


def led_off():
    GPIO.output(LED_PIN, False)


def is_internet_on():
    """Check connection to api_host"""
    try:
        urllib2.urlopen(API_HOST, timeout=1)
        return True
    except urllib2.URLError as err:
        pass
    return False


def is_door_open():
    """Check if the door is open"""
    response = urllib2.urlopen(API_HOST)
    data = json.loads(response.read())

    if type(data) == list:
        data = data[0]

    return data['isOpen']['door']


if __name__ == "__main__":
    main()

