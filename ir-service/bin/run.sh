#!/bin/bash

./boot.sh

# Block script completion to hold open docker container
while true; do
	sleep 30d
done
