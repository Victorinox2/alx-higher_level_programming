#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays
the value of X-Request-Id variable
found in the header of the response.
"""
from urllib.request import urlopen
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    with urlopen(url) as response:
        header = response.headers

        x_request_id = header['X-Request-Id']
        print(x_request_id)
