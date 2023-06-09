import urllib.request, urllib.parse, urllib.error

URL = "https://www.github.com"
PROXY_ADDRESS = "165.24.10.8:8080"  # By Googling free proxy server


if __name__ == "__main__":
    proxy = urllib.request.ProxyHandler({"http": PROXY_ADDRESS})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(URL)

    print(f"Proxy server returns response headers: {resp.headers}")
