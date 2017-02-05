#!/bin/bash

# Setup Data Directory
mkdir -p /var/data/ir-service/commands
mkdir -p /var/run/lirc
chown -R www-data:www-data /var/data/ir-service
chown -R root:root /var/run/lirc

# Run confd to write out configuration files
confd -onetime -backend env
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/ir-service /etc/nginx/sites-enabled/ir-service
ln -s /etc/uwsgi/apps-available/ir-service.ini /etc/uwsgi/apps-enabled/ir-service.ini

sudo /usr/sbin/lircd --driver=default --device=/dev/lirc0
service uwsgi restart
service nginx restart
