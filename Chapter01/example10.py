# 인터넷 시간 서버로부터 현재 시간을 얻은 후 출력

import ntplib
from time import ctime


def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request(("pool.ntp.org"))
    print(ctime(response.tx_time))


if __name__ == "__main__":
    print_time()
