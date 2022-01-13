"""
1.爬取专利数据
2.将数据存储到数据库
"""
import requests
import json
import csv

if __name__ == "__main__":
    # 获取每一页的数据
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Connection': 'keep-alive',
        'Accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / avif, image / webp, '
                  '* / *;q = 0.8',
        'Referer': 'https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord'
    }
    u = 'https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord'
    r = requests.get(url=u, headers=h)
    c = r.cookies

    # https://aiqicha.baidu.com/detail/patentAjax?p=5&size=10&pid=13100503229410
    u = 'https://aiqicha.baidu.com/detail/patentAjax'
    p = {"p": 1, "size": 10, "pid": "13100503229410"}
    r = requests.get(url=u, params=p, headers=h, cookies=c)
    rs = json.loads(r.text)
    d = rs['data']['list']  # 得到需要的数据
    '''
     需要获取的信息
     'patentName': '基于主成分分析优化的差分隐私高维数据发布保护方法',
     'publicationNumber': 'CN110334546B',
     'patentType': '发明专利',
     'publicationDate': '2021-11-23',
     '''
    # 将数据转换为csv文件
    with open("D:\\Program Files (x86)\\project\\tmp_py\\pc.csv", "w", encoding="utf_8_sig", newline="") as cf:
        wr = csv.writer()
        wr.writerow(d[0].keys())
        for r in d:
            wr.writerow(r.values)

    print(rs)
