import requests
import execjs

session = requests.session()
headers = {
    'authority': 'www.python-spider.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
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
with open('match2.js', 'r', encoding='utf-8') as f:
    js_text = f.read()
    cookie = execjs.compile(js_text).call('match2_SDK')
cookies = {
    'm': cookie.split(';')[0].replace('m=', '')
}


def get_count(page):
    if page >= 4:
        headers['User-Agent'] = 'yuanrenxue.project'
    response = session.get(f'https://match.yuanrenxue.com/api/match/2?page={page}', cookies=cookies, headers=headers,
                           verify=False).json()
    data = response['data']
    count = 0
    for d in data:
        # print(d)
        num = int(d['value'])
        count += num
    print(count)
    return count


if __name__ == '__main__':
    result = 0
    for i in range(1, 6):
        c = get_count(i)
        result += c
    print(result)
