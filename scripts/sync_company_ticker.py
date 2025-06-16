# -*- coding: UTF-8 -*-

import logging
import requests  # 发送请求

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "_ga=GA1.1.683960344.1749707305; nmstat=175cc488-2c28-1609-e5f9-444923491bcc; _ga_300V1CHKH1=GS2.1.s1749707305$o1$g1$t1749707504$j57$l0$h0; _ga_CSLL4ZEK4L=GS2.1.s1749707305$o1$g1$t1749707504$j57$l0$h0; ak_bmsc=17D52E7A890B0FC3C696A2922B62B5A8~000000000000000000000000000000~YAAQCyoSAq1J4liXAQAARY1RdxwlA1h3IvDea8npc3u/h4poeX8CBV287s4x1GfiCVfejTlu6LvHn3nI70jGP1cx10b/Rza8VtXDSrkGfbjJSfcMP522ohVoiQLhPJn3w+ZhbjeQybJDjGnSktZTE/y5OT6btKeszd7VXorvsNaLnLmkOOHcM5HBz56Xf0HRosGQkwGHE7qIwlyjmoqJHGKpix+C6d1125hr706IJQ3teJw+pwvFgV/+xVWRtxGFrXscljPHoKUuLmTgNn1VdoFEW3aTWGCkABljW67J9iiJFqDQJuO5oGFUszE2a5itM0vGLEVjoXm/qeT5mOSiXKnkEnB+bMQLesbdCtwYN8K1Uoyn7qp4JUvZZxpTdGrhUTaPb2HrR3QF; bm_sv=B89C925ABA0A72218BDDB0F96F201509~YAAQCyoSApRN4liXAQAAdAdSdxw9BYDW0+RWP54cKoUpLtWj3iNTwyVYV8pJYThPWSh3WArFu964cSF2Xy0remOU4XNqdmcB1Fb09Wb+m/y+lLn7hyyHTzV0+PWuHwqA6NY/P3Z6L3YaMqVyVx21Xrv5aUZNKzDP+FwehnRzaHL+yqo8VwM86+2MfM997WCCei7+6EzEYkPgGT0l5bxxYlh2JLpJjacwPtnMPdRdHD33+eGVmNn+I2I7gFWv~1",
}


def run():
    # 使用requests发送GET请求
    response = requests.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers=headers,
    )

    if response.status_code == 200:
        body = response.text
        print("company_ticker: ", body)
        with open("company_ticker.json", "w") as f:
            f.write(body)
    else:
        print("ticker request error: ", response)


try:
    run()
except Exception as e:
    print("ticker exec error: ", repr(e))
    logging.exception(e)
