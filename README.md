# hackerspace-door light
door_status_led.py is a simple program that queries the API at 
http://hackerspace.idi.ntnu.no/api/door and controls a LED-light showing on whether the
door to the hackerspace is open. If the script fails to contact the API, it will turn the LED off. 

## Installing dependencies.

You only need [RPi.GPIO]:

	$ wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.1.0.tar.gz
  	$ tar zxf RPi.GPIO-0.1.0.tar.gz
  	$ cd RPi.GPIO-0.1.0
  	$ sudo python setup.py install

## Setup
 
To make the script door_status_led.py run at boot, add 'python /"path"/DoorOpenLED/door_status_led.py' to /etc/rc.local.

Then connect a LED light in series with a resistor between gpio 7 and ground.
## Make init daemon
- copy door_status_led to /etc/init.d
- update initrc
    update-rc.d /etc/init.d/door_status_led defaults
