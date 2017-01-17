#!/bin/bash

# Run confd to write out configuration files
confd -onetime -backend env
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/ir-service /etc/nginx/sites-enabled/ir-service
ln -s /etc/uwsgi/apps-available/ir-service.ini /etc/uwsgi/apps-enabled/ir-service.ini

service uwsgi restart
service nginx restart

# Block script completion to hold open docker container
while true; do
	sleep 30d
done
