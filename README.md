# hackerspace-door light
door_status_led.py is a simple program that queries the API at 
http://hackerspace.idi.ntnu.no/api/door and controls a LED-light showing on whether the
door to the hackerspace is open. If the script fails to contact the API, it will instead
flash the led for half a second. 

## Installing dependencies.

You only need [RPi.GPIO]:

$ wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.1.0.tar.gz
$ tar zxf RPi.GPIO-0.1.0.tar.gz
$ cd RPi.GPIO-0.1.0
$ sudo python setup.py install

Then to make the script door_status_led.py run at boot add
 'python /"path"/DoorOpenLED/door_status_led.py'
  to /etc/rc.local 

Then connect a LED light to gpio 7.