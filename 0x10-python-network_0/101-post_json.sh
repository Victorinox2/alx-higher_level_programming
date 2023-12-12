#!/bin/bash

# This script sends a JSON POST request to the provided URL with the contents of a file in the body.

url=$1
file_path=$2

# Use curl to send a JSON POST request with the contents of the file in the body
curl -s -X POST -H "Content-Type: application/json" -d "@$file_path" "$url"
