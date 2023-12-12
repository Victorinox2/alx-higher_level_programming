#!/bin/bash
# This script takes a URL as an argument, sends a GET request, and displays the body of 200 status code response.

curl -sL "$1"
