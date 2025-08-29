# -*- coding: UTF-8 -*-

import logging
import requests  # 使用requests库替代urllib

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
    "cookie": "ak_bmsc=D13E24CF001C6F8FBFC8A6BB9801437B~000000000000000000000000000000~YAAQpoA3Fxde/tOYAQAADXjX8xy68qhnXFW56LAlcyexll/p6CEfTpjPAKQQx0K/heOa8eHUUGV1szfbvAwYal62wEXNZhdP0JP7cYtqg0peYHTMob63M0LuWxIVB4P8QSUtiCJOImQ9cfuP0xOU4lKzAy9ehs/MYs+KMUz/OHnNjAydU03tqIq/m1ZV8Gc2n7Ccogyy4oyrKbPWzxk4izW4xdebTwoBrQWDuv2Jvz5Ag+Gs75cQjJYEZG/amdT3zh5ij57OljPOaNRISUQQLDnTEmlMFYZ++0SmtPrQIwARAhyFrurwKOaBLEpfhqnel8PuTb2NSM7tVqeUfN5y4gEsjZlsvxkxcvtp09gA7bz0GBUWDYV+ebW4PGwwX7T5+OVKCO9DLw==; bm_sv=5CBCBDEC9C9344E8659924C01F702ACB~YAAQpoA3F3fa/tOYAQAAKljY8xxdJaGV1RkDp7WJbMdk1rP0Ku5AqMLH4wWn+3Bfd2J2B9IzpvXESh79YtZfBsH8zzl+IqfOh66WOYCFSdKA03X+GM8aeZN3fuUPMD/Jja60vTerwf2pXcDcuPQxtACHQb/v9uqIdRP/QEQce7hVeBDjDeEpvRoWTZoTPa9AWlNI0nosR+mFDFKOkMvrOGUC8I8rlRNKFHfnDFFCxIv0G3l3S7kulspS6TPC~1"
}


def run():
    # 使用requests发送GET请求
    response = requests.get("https://www.sec.gov/include/ticker.txt", headers=headers)

    if response.status_code == 200:
        body = response.text
        print("ticker: ", body)
        with open("ticker.txt", "w") as f:
            f.write(body)
    else:
        print("ticker request error: ", response)


try:
    run()
except Exception as e:
    print("ticker exec error: ", repr(e))
    logging.exception(e)
