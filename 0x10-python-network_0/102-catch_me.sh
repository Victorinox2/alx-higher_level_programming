#!/bin/bash

# This script makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with a message.

url="http://0.0.0.0:5000/catch_me"

# Use curl to make a request and cause the server to respond with specific message
curl -s -L -X PUT "$url" -d "user_id=98" -H "Origin: HolbertonSchoo"
