import http.cookiejar
import urllib


ID_USERNAME = "id_username"
ID_PASSWORD = "id_password"
USERNAME = "username"
PASSWORD = "password"
LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
NORMAL_URL = "https://bitbucket.org/"


def extract_cookie_info():
    # setup cookie jar

    cj = http.cookiejar.CookieJar()
    login_data = urllib.parse.urlencode(
        {ID_USERNAME: USERNAME, ID_PASSWORD: PASSWORD}
    ).encode("utf-8")
    # create url opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    resp = opener.open(LOGIN_URL, login_data)

    # send login info
    for cookie in cj:
        print(f"----First time cookie: {cookie.name} --> {cookie.value}")
    print(f"Headers: {resp.headers}")

    # now access without any login info
    resp = opener.open(NORMAL_URL)
    for cookie in cj:
        print(f"++++Second time cookie: {cookie.name} --> {cookie.value}")

    print(f"Headers: {resp.headers}")


if __name__ == "__main__":
    extract_cookie_info()
