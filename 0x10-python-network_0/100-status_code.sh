#!/bin/bash

# This script sends a request to the provided URL and displays only status code.

url=$1

# Use curl to send a request to the provided URL and print only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$url"
