#!/bin/bash
# This script takes a URL as an argument, sends a POST request with specific variables, and displays the body of the response.

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST -d "email=$email&subject=$subject" "$url"
