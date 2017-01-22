# tv-service

## Description
*tv-service* is a Python Flask service to run on the Raspberry Pi.
It's primary purpose is to provide an REST API for communicating with a TV 
over IR.

## How to Run
* Run `docker build -t tv-service .`
* Make note of the created containers __imageId__
* Run `docker run -p 5000:5000 -d __imageId__`
* Open web browser to http://localhost:5000




# Getting LIRC Running on Raspbian Jessie

* sudo systemctl stop lirc
* Make a backup of /etc/lirc/hardware.conf
* Make a backup of /boot/config.txt
* Make a backup of /etc/lirc/lircd.conf
* Open /etc/lirc/hardware.conf and modify the following lines to match:
```
LIRCD_ARGS=”–uinput –listen”
DRIVER=”default”
DEVICE=”/dev/lirc0″
MODULES=”lirc_rpi”
```
* Open /boot/config.txt to add dtoverlay=lirc-rpi,gpio_in_pin=18,gpio_out_pin=17
* sudo systemctl start lirc
* sudo /usr/sbin/lircd --driver=default --device=/dev/lirc0 
* Test receiving with:
```
mode2 -d /dev/lirc0
```
* If receiving functional move on.
* sudo systemctl stop lirc
* Record a few remote keys with:
```
irrecord -d /dev/lirc0 ~/lircd.conf
```
* Copy ir config to lirc:
```
sudo cp ~/lircd.conf /etc/lirc/lircd.conf
```
* sudo systemctl restart lirc

* If setup correctly following should print out the configured buttons:
```
irsend LIST /home/pi/lircd.conf “”
```
* Try sending an IR command:
```
irsend SEND_ONCE /home/pi/lircd.conf KEY_DOWN
```
