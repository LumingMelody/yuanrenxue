import re

import requests
import execjs

headers = {
    'authority': 'www.python-spider.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
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


def get_count():
    url = 'https://www.python-spider.com/challenge/11'
    cookies = {
        'sessionid': 'eez3f668zsxgalch10ddtgxjzf59v6y1',
    }
    session = requests.session()

    resp = session.get(url, cookies=cookies, headers=headers)

    js_code = re.match(r'<script>(.*)</script>', resp.content.decode()).group(1)

    sdk = """
        function jsl_SDK(js_text) {
        setTimeout = function () {
        };
        document = {};
        document.cookie = "";
        location = {};
        location.pathname = '/challenge/11';
        location.search = "";
        document.createElement = function (val) {
            return {
                innerHTML: "",
                firstChild: {
                    href: 'https://www.python-spider.com/',
                },
            }
        };
    
        window = global;
        window.addEventListener = function () {
        };
        document.addEventListener = function (a, b, c) {
            b()
        };
        document.attachEvent = function () {
        };
        eval(js_text)
        return document.cookie
    }
    """
    result = execjs.compile(sdk).call('jsl_SDK', js_code)
    # print(result)
    cookies['__jsl_clearance'] = result.split('=')[1].split(';')[0]
    # print(cookies)
    response = session.get(url, cookies=cookies, headers=headers)
    print(response.text)
    data = re.findall(r'<td class="info">(.*?)</td>', response.text, re.S)
    # print(data)
    nums = 0
    for d in data:
        num = d.strip()
        print(num)
        num = int(num)
        nums += num
    print(nums)


if __name__ == '__main__':
    get_count()