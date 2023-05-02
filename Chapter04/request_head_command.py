import argparse
import http.client
import urllib.parse
import re
import urllib.request, urllib.error

DEFAULT_URL = "http://www.python.org"

HTTP_GOOD_CODES = [http.client.OK, http.client.FOUND, http.client.MOVED_PERMANENTLY]


def get_server_status_code(url):
    """Download just the header of a URL and return the server's status code."""
    host, path = urllib.parse.urlparse(url)[1:3]
    try:
        conn = http.client.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status

    except Exception as e:
        print(f"Server: {url} status is: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example HEAD Request")
    parser.add_argument("--url", action="store", dest="url", default=DEFAULT_URL)
    given_args = parser.parse_args()
    url = given_args.url
    if get_server_status_code(url) in HTTP_GOOD_CODES:
        print(f"Server: {url} status is OK: {get_server_status_code(url)}")
    else:
        print(f"Server: {url} status is NOT OK: {get_server_status_code(url)}")
