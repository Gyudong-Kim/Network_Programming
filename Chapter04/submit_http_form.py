import requests
import urllib

ID_USERNAME = "id_username"
ID_EMAIL = "id_email"
ID_PASSWORD = "id_password"
USERNAME = "username"
EMAIL = "email"
PASSWORD = "password"
SIGNUP_URL = "https://twitter.com/account/create"


def submit_form():
    """Submit a form"""
    payload = {
        ID_USERNAME: USERNAME,
        ID_EMAIL: EMAIL,
        ID_PASSWORD: PASSWORD,
    }

    # make a get request
    # resp = requests.get(SIGNUP_URL)
    # print(f"Response to GET request: {resp.content}")

    # send POST request
    resp = requests.post(SIGNUP_URL, payload)
    print(f"Headers from a POST request response: {resp.headers}")


if __name__ == "__main__":
    submit_form()
