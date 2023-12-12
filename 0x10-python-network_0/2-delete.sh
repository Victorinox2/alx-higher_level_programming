#!/bin/bash
# This script sends a DELETE request to the provided URL and display body of the response.

curl -s -X DELETE "$1"
