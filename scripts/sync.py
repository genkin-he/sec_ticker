# -*- coding: UTF-8 -*-

import logging
import requests  # 使用requests库替代urllib
import time

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; SECBot/1.0; +https://www.sec.gov/developer)",
    "Accept": "text/plain, application/json, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}


def run():
    # 使用requests发送GET请求
    response = requests.get(
        "https://www.sec.gov/include/ticker.txt", 
        headers=headers,
        timeout=30
    )

    print(f"Response status: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")

    if response.status_code == 200:
        body = response.text
        print("ticker: ", body[:200] + "..." if len(body) > 200 else body)
        with open("ticker.txt", "w") as f:
            f.write(body)
    else:
        print("ticker request error: ", response)
        print("Response content: ", response.text)


try:
    run()
except Exception as e:
    print("ticker exec error: ", repr(e))
    logging.exception(e)
