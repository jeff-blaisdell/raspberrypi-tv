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

