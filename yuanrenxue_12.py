
import execjs
import re
import requests


session = requests.session()

response = session.get('https://match.yuanrenxue.com/match/13', verify=False)
print(response.content.decode())

# 构造要执行的JS代码
js_code = f"""
    document = new Object();
    location = new Object();
    function result(){{
    {re.match('<script>(.*)</script>',response.content.decode()).group(1)};
    return document.cookie
}}
"""

cookie = execjs.compile(js_code).call('result')
print(cookie)