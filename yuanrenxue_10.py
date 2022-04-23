import requests
import execjs


session = requests.session()
headers = {
    'authority': 'www.python-spider.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1650444183; no-alert=true; sessionid=mdfx5n765zjo6vy5pbdtiqihfgpw3hpb; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1650458466',

    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'If-None-Match': '"I3DYucBdy4F94HgmETB5zOzEB7k="',
    'Referer': '',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.python-spider.com',
    'referer': 'https://www.python-spider.com/challenge/10',
    'x-requested-with': 'XMLHttpRequest',
    'Origin': 'https://www.python-spider.com',
    'If-Modified-Since': 'Sat, 12 Feb 2022 07:59:18 GMT',
}
session.headers = headers
data = {
  'page': '1'
}

response = session.post('http://www.python-spider.com/challenge/10', data=data, verify=False)
print(response.content.decode())
