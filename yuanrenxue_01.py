import time
import hashlib
import requests
import base64
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(['标题'])

cookies = {
    'HMACCOUNT_BFESS': '50E7B7959220712A',
    'BAIDUID_BFESS': '3A9CE933362C0069185DC0C2CD652965:FG=1',
}

headers = {
    'authority': 'www.python-spider.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'Hm_lvt_337e99a01a907a08d00bed4a1a52e35d=1650614987; sessionid=yticiuv0i9e232h8d0uv0huys0legwb4; Hm_lpvt_337e99a01a907a08d00bed4a1a52e35d=1650615530',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'referer': 'https://www.python-spider.com/challenge/1',
    'safe': 'e202094c3cea9dbae4b48369a46337fb',
    'timestamp': '1650615529',
    'x-requested-with': 'XMLHttpRequest',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'If-None-Match': '2f653f7a6435d29018fb389d907b40e2',
    'Referer': 'https://www.python-spider.com/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'content-length': '0',
    'origin': 'https://www.python-spider.com',
}


# base64解码函数
def E_BASE64(origStr):
    dStr = base64.b64encode(origStr.encode())
    return dStr


def get_count(page):
    m = hashlib.md5()
    a = '9622'
    timestamp = str(time.time()).split(".")[0]
    str1 = a + timestamp
    str2 = E_BASE64(str1)
    print(str2)
    m.update(str2)
    safe = m.hexdigest()
    headers['safe'] = safe
    headers['timestamp'] = timestamp
    response = requests.get(f'https://www.python-spider.com/challenge/api/json?page={page}&count=14', headers=headers,
                            cookies=cookies).json()
    infos = response['infos']
    for info in infos:
        message = info['message']
        ws.append([message])
    wb.save(r"./count.xlsx")


if __name__ == '__main__':
    for i in range(1, 86):
        # print(i)
        get_count(i)
