import time

import execjs
import requests

headers = {
    'authority': 'www.python-spider.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1650612562; no-alert=true; sign=1650614341~YWlkaW5nX3dpbjE2NTA2MTQzNDEzNTI=|e3f7c87420b21c87d0fe9bed0ef9698a; sessionid=x836w64bmphyc2lucwae23grpbk196um; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1650705952',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.python-spider.com',
    'referer': 'https://www.python-spider.com/challenge/14',
    'x-requested-with': 'XMLHttpRequest',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'If-None-Match': '3f99a1f32c9431cd3e101d0fdcd53a12',
    'Referer': 'https://www.python-spider.com/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

data = {
    'page': '1',
    'uc': 'TCz1BS3BYvAu+wyfQd/tdg==',
}


def get_uc(page):
    with open('challenge_14.js', 'r', encoding='utf-8') as f:
        js_text = f.read()
    uc = execjs.compile(js_text).call('get_uc', page)
    return uc


session = requests.session()


def get_count(page):
    data['page'] = page
    data['uc'] = get_uc(page)
    print(data)
    response = session.post('https://www.python-spider.com/api/challenge14', headers=headers,
                            data=data).json()
    print(response)
    count = 0
    for d in response['data']:
        num = int(d['value'])
        count += num
    return count


if __name__ == '__main__':
    result = 0
    for i in range(1, 101):
        print(i)
        r = get_count(i)
        # time.sleep(0.5)
        result += r
    print(result)
