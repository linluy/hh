import csv
import json
import time

import requests

if __name__ == '__main__':
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Connection': 'keep-alive',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer': 'https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord'
    }
    # 模拟人的行为---首先找到辽宁工业大学的主页
    # https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord
    u = "https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord"
    r = requests.get(url=u, headers=h)
    c = r.cookies
    print('c______________________',r.cookies)

    # https://aiqicha.baidu.com/detail/intellectualPropertyAjax
    u = "https://aiqicha.baidu.com/detail/patentAjax"
    p = {"p": 1, "size": 10, "pid": "13100503229410"}
    r = requests.get(url=u, params=p, headers=h, cookies=c)
    j = json.loads(r.text)
    print(j)
    # ['copyright']
    s = j['data']['pageCount'] + 1
    print(s)
    t = ['patentName', 'referId', 'publicationNumber', 'patentType']

    # # excel
    # with open('s.csv', 'w', encoding="utf_8_sig", newline='') as cf:
    #     wr = csv.writer(cf)
    #     wr.writerow(t)
    #     u = "https://aiqicha.baidu.com/detail/patentAjax"
    #     for i in range(1, s):
    #         p = {"p": i, "size": 10, "pid": "13100503229410"}
    #         r = requests.get(url=u, params=p, headers=h, cookies=c)
    #         j = json.loads(r.text)
    #         for r in j['data']['list']:
    #             l = [r['patentName'], r['referId'], r['publicationNumber'], r['patentType']]
    #             wr.writerow(l)
    #         time.sleep(0.1)
