#!/bin/bash
# This script takes a URL as argument and displays all HTTP methods the server will accept.

curl -sI "$1" | grep -i allow | awk '{print $2}'
