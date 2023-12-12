#!/bin/bash
# This script takes a URL as argument, sends a GET request with a specific header, and displays the body of the response.

url=$1
user_id_header="X-School-User-Id: 98"

curl -s -H "$user_id_header" "$url"
