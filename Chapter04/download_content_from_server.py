import argparse
import urllib.request
import requests
import httplib2

HOST = "http://www.cnn.com"


class HTTPClient:
    def __init__(self, host):
        self.host = host

    def fetch_by_requests(self):
        response = requests.get(HOST)
        return response.text

    def fetch_by_urllib(self):
        response = urllib.request.urlopen(HOST)
        return response.read().decode()

    def fetch_by_httplib2(self):
        http = httplib2.Http()
        (response, content) = http.request(HOST, "GET")
        print(response)
        return content.decode()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Client Example")
    parser.add_argument("--host", action="store", dest="host", default=HOST)

    given_args = parser.parse_args()
    host = given_args.host
    client = HTTPClient(host)
    print(client.fetch_by_requests())
    print(client.fetch_by_urllib())
    print(client.fetch_by_httplib2())
