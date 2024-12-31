# -*- coding: UTF-8 -*-

import logging
import urllib.request  # 发送请求
import gzip

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "ak_bmsc=58A73C16BE174431B4AA498FD3149148~000000000000000000000000000000~YAAQONgjF5rRj6+SAQAAilNivRnbWcLgb+diTqn7rG7kYL+fnlgynQ3zHq1Yw3BcoQQGuQJxuLPudtXgu1qFjZgqoq8V2jHXiLXYeDZBUEA4ukZ0kIMZjMWHaEzdX0uTMSPwZFB6QuB2jjgIH62a3Itp584y56gzber2AIo0qQvFflZ3dGS4yq1ghOB3rUrDfnpgAEFc6Y/c+dXRqfu9ZaBHfCJH7ZzPlD1qBmbAnlOT3rR6tT/SHev4xYpwNS8ckEiVv/4Ueun/F+i1DfcLKBbzzakt0Fq4mkiOGA7/Z0M6/+NfODqK2PUTMUcF+zPu3N4uJ1/yLmXmZJCYDAUcdxiurqGcHBavQ/W8I2VZ65ICNDAW2zW2OWBot1zTcqTB7/30jb2omA==",
}

def run():
    # request中放入参数，请求头信息
    request = urllib.request.Request(
        "https://www.sec.gov/files/company_tickers.json",
        None,
        headers,
    )

    # urlopen打开链接（发送请求获取响应）
    response = urllib.request.urlopen(request)
    if response.status == 200:
        body = response.read().decode("utf-8")
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
