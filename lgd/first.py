import csv
import json
import requests

if __name__ == '__main__':
    h = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Connection':'keep-alive',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer':'https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord'
    }
    # 模拟人的行为---首先找到辽宁工业大学的主页
    # https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord
    u = "https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord"
    r = requests.get(url=u,headers=h)
    c = r.cookies
    print("c:----------",c)
    # 找到专利这一项，一共2082个专利
    # https://aiqicha.baidu.com/detail/intellectualPropertyAjax
    u = "https://aiqicha.baidu.com/detail/intellectualPropertyAjax"
    p = {"pid": "13100503229410"}
    r = requests.get(url=u, params=p, headers=h, cookies=c)
    j = json.loads(r.text)
    # 不大懂
    t = j['data']['patent']['total']
    print("j:----------", j)
    # 得到第几页的专利信息
    #  https://aiqicha.baidu.com/detail/patentAjax
    u = "https://aiqicha.baidu.com/detail/patentAjax"
    p = {"p": 1, "size": 10, "pid": "13100503229410"}
    r = requests.get(url=u, params=p, headers=h, cookies=c)
    j = json.loads(r.text)
    d = j['data']['list']
    print("d:----------", d)

    # excel
    with open('w.csv','w+',newline='') as cf:
        wr = csv.writer(cf)
        wr.writerow(d[0].keys())
        for r in d:
            wr.writerow(r.values())