# Goal: sync https://www.sec.gov/include/ticker.txt
cookie='nmstat=0aadcbd0-38a7-0e6e-d394-d841487c925b; _ga=GA1.2.2114479356.1719919118; _ga_300V1CHKH1=GS1.1.1719974757.1.1.1719975074.0.0.0; _4c_=%7B%22_4c_s_%22%3A%22lVPBbtswDP2VQucosWRZsnMbOmDYIRs2dLsWikTHRtPIkNW4XZB%2FH2k7RZduhwUGYj4%2BPj2T4okNDRzYWhhRVabI6NEL9gAvPVufWGw9%2FR3ZmhUFiFI4yWtV51wZpfhWe8FzpSotlCwqmbEFeyYtaXRVCFGWJj8vmOtmjRNzwQNqiWopymXG6x4r0i9EVEnFXQz%2ByaX79NIRbYDtTe8fMOHh2Dq4H1qfmrF%2BPGtGG2h3TSI4G1V8FzGQ%2BDa0Bx%2BG67IZfS2rcoXoNoahB6q8bWJ4hBshNcIB%2B8A21uFrhBpiHCkY9W0ijz245S4cZwD7NmF8wn62hPqbu9vviH95g3y7%2FbqZoe44290HZ%2FckihNZsE8f7n98%2FkgpIZQyVV7o5TgmUWFrkfAU95htUur69Wo1DMNyNrM6wNDHEB5XXYS%2B5xH2YHugZsOBDuuiJ8PgUhsOk2GM72K720HcQGoCjh1j61ti2D11lYgRPPTtjux5ah1GDyl0r%2FD5cgGyDO%2BE1qqSOOCEPkutMvqdp%2B8d74N8yxaFMVq%2FZ09z4dRTOPxf6bG9XF6Rw1Za7bh0znIlLfAtSMGNssLnVutC15fLS4uAcSZUNUuK8qLoob5IlmBzVRvNRQYl7YPkWJfzbKuhNMpnTlh25bIy2XuX1NhJ8k135zUaNxLLFPLaLs3EyaMyBe6X%2BJNLCHEvkpb9NR%2BHV6kpMX%2Fu8xVC04pXp%2F6Lej7%2FBg%3D%3D%22%7D; _ga_CSLL4ZEK4L=GS1.1.1719974758.1.1.1719975075.0.0.0; ak_bmsc=C237056F07A5A27137F946A1199039AE~000000000000000000000000000000~YAAQGFLIFzw/sJ2QAQAANrIUoRhfXZZrVkfQo9T/7BNW+/zezFsf5IT6dCpwf3yt04pQJu5mYZvAcCZ+CvXSg/6Xg1VyZHWt4kUe9yqnXKtSvt7QcBMjYtRnuzRn4AqkOsNRZ6lu/Z1scPYwtlC6h0nbCIHSfdMCmDo1I0hSUf6dDyrTnrMuPxItzbqrvPnggvFvlb/9MKY1Jfe8UW0x8iDQ4UsnYdWPJEifK+Wk+AtoK6Quh6VEYmAznL8A+VmSvOMCygKLcF4C8TMolCNrnVVc6QtClYEBh00+UgJxQ7lo+54kL15QrzOEsNoi9yZuli0VJOnRkJT8jAYMVc4Mt7JcKshLlrD4SVUJZbyP3UGEdjVM4fVb5EQcYFRhsY2wps7dlCC0Z4vh'
curl --request GET https://www.sec.gov/include/ticker.txt --header \
"cookie: $cookie" --header \
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"  --header \
'Accept-Encoding: gzip, deflate, br, zstd'  --header \
'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8'  --header \
'Cache-Control: no-cache'  --header \
'Dnt: 1'  --header \
'Pragma: no-cache'   --header \
'Priority: u=0, i'  --header \
'Sec-Ch-Ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"'  --header \
"Sec-Ch-Ua-Mobile: ?0"  --header \
'Sec-Ch-Ua-Platform: macOS'  --header \
"Sec-Fetch-Dest: document"  --header \
"Sec-Fetch-Mode: navigate"  --header \
"Sec-Fetch-Site: none"  --header \
"Sec-Fetch-User: ?1"  --header \
"Upgrade-Insecure-Requests: 1"  --header \
"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" -o ./ticker.txt
