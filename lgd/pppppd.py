# -*- coding: utf-8 -*-
"""
get from baidu
"""
import csv

import requests
import json
import time
import bs4
import datetime
import pymysql


def inDB(data):
    db=pymysql.connect(host='localhost',user='root',password='123456',database='lgd')#打开数据库
    cursor=db.cursor()
    # sql = 'insert into t_zl (getDate,getTime,zlmc,sqh,sqrq,gbh,gbrq,fmr,zlsqr,zldlr,zldljg,zllx,flh,address,flzt)'
    sql = 'insert into t_zl_data (getDate, getTime, zlName, sqNumber, sqDate, gbNumber, gbDate, fmPerson, zlsqPerson, zldlPerson, zlAgency, zlCategory, flNumber, address, flStatus)'
    sql += "values " + str(tuple(data))
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(str(e))
    db.close()


if __name__ == "__main__":
    u = "https://www.baidu.com/"
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        # 让网站认识你
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Referer': 'https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord',  # 解决爬虫
        'Accept-Encoding': 'gzip, deflate, br'
        # 'Cookie': 'BIDUPSID=A6F7C19298AA48195ED1C8D9D5C1AEE5; PSTM=1625451732; __yjs_duid=1_749d91ea64faf6aac9a31b55a906fe4f1625453415448; BAIDUID=C41171408150F2384200B72AEDBC0466:FG=1; BDUSS=Th4bFg2N2x2RzZtZ2J2ZnNNfmViTnh1Ym1RNHZ1VjA1QWFUaEw4d3pvdH44ZHhoRVFBQUFBJCQAAAAAAAAAAAEAAACYfj8ONDQ3MTA2MTIyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH9ktWF~ZLVhe; BDUSS_BFESS=Th4bFg2N2x2RzZtZ2J2ZnNNfmViTnh1Ym1RNHZ1VjA1QWFUaEw4d3pvdH44ZHhoRVFBQUFBJCQAAAAAAAAAAAEAAACYfj8ONDQ3MTA2MTIyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH9ktWF~ZLVhe; BDPPN=86a60a08aa31dfcbfafede702c1fd0a2; _j54_6ae_=xlTM-TogKuTw0X0DQQxoN6VXOWGXa-YmJwmd; log_guid=ae08cfad87b608af0955dd2d81706ff0; _j47_ka8_=57; BAIDUID_BFESS=F3B85BFA5AB02BB209391C1043CBE8FA:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_st=2_YTE3MzQ0NmRkNWIyOGQxYjYwZTljZjczNWQzMTk2ODk3ZWJmZWU4ZWNhMmRkODVkYzYyNDM2YTk2NTExMTUyNjk0OTUxZGE3MDA1NmI3N2I2MjA3MGY2MTgxNTdiNTMzMzE5OGEyMmJhMTY2ZTI0Y2MxNGQxMDY0MWJlNjNiMWJlYTg4YzAwOGNjN2M2NzUzNmJkZGMyOGU4ZTAzMzFiNDRhNDllODE5MjRhMzAyOGJiODcwOWZkODUyMjg2NmVmOWJkZThkNmNhMTY5OGFkZjc3Yzg0YWU1YjY4ZGFiZDJkMWYzNjY4OTc4NDgyNzZlNTU0YTBlMTM4YjVlNWM3MDZmYzRhNzg2YmQ5MDMyY2QzOWU0Y2E3M2UxMGViYTU5XzdfZWI0MDY4ZjU=; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; H_PS_PSSID=35411_34445_35105_31253_35629_34584_35490_35245_35664_35315_26350_35620_35562; BA_HECTOR=8l05a4848h2ha005ka1gta7pn0q; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1641178648,1641183074,1641189731,1641357119; _fb537_=xlTM-TogKuTw7r5KZUhlTslPDQ8M05J32iJ1ffpPd8oMu1WMZqdivIgmd; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1641357260; ab_sr=1.0.1_MjE1MWJiMTkzNmI1YTVkNzk0ZTczZjk5MWViMDAwODUzOWNjN2UxMjc3ZGMwMGM1ZTFkMTk4NzU1NmMxZGFmNzI2NzJjOTRhYzU3OWIwNzEwYzlhZmVhYzRmNzhjNTc3NTg4MTk0Zjc0ZWUzNTliYzYxYmM0MDMwZjA1NTYzYjJmYTQyYjc4NTYwYWM5OWFmOGYzOTg2ZDhhZTFmMGU4NWQ4NGZhZTJmYjk0ZDJmMmVjOWVlYTYxY2NkNDJjNWI2; _s53_d91_=e27d644896d1800d6f2981fcb981e321adea0c9c207d962fd7fd1650b06e7c64d352812de00d5ecddceb68e28b0a043728854d1e11f7ea926a62578efcf5416ce1687d743fa68feb0019ccb826d7d4bd874b47fe66d08e31c94b7a0ce08396c0ea00167fe2e6ee6963d927eecb21771169bac0c0ac134169cf488e32785f02c207c35e7793c1883a13ba23223619cd7b0eaefb981916a12ee3f4d19cfe4a13fc9b68bcfe70caf9c6b64ee9decb3debee95c5805f20525b358ade6d37900c443d996863700cded4b8f73ddd9821087d6060f239181d2e37cd423377500ffe12e9; _y18_s21_=26d26bbc; RT="z=1&dm=baidu.com&si=ol5yjicj2nt&ss=ky11nd8h&sl=p&tt=jvs&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=359m"'

    }
    r = requests.get(url=u, headers=h)
    c = r.cookies

    u = "https://aiqicha.baidu.com/detail/patentAjax"
    p = {"p": 1, "size": 10, "pid": "13100503229410"}
    r=requests.get(url=u, params=p, headers=h, cookies=c)
    print('r-----', r.text)
    j = json.loads(r.text)
    t = j['data']['pageCount']
    rids = []
    with open("s.csv", "r", encoding="utf_8_sig", newline="") as cr:
        d = csv.reader(cr, delimiter=',')
        for r in d:
            rids.append(r[1])
    el = []
    count = 0
    # for i in range(184, t + 1):
    #     p = {"p": i, "size": 10, "pid": "13100503229410"}
    #     r = requests.get(url=u, params=p, headers=h)
    #     j = json.loads(r.text)
    #     d = j['data']['list']
    #     for l in d:
    #         Rids.append(l['referId'])
    #     time.sleep(0.5)
    #     print('爬取进度：' + str(i / 208))
    for i in rids:
        u = "https://www.baidu.com/"
        r = requests.get(url=u, headers=h)
        # c = r.cookies
        u = "https://aiqicha.baidu.com/patent/info"
        p = {'referId': i, 'pid': '13100503229410'}
        r = requests.get(url=u, params=p, headers=h, cookies=c)
        if (r == None):
            print('none')
        s = bs4.BeautifulSoup(r.content.decode("utf-8"), "lxml")
        t = s.find_all('tr')
        a = []
        a.append(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))  # getDate 当前时间的时间戳
        print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        a.append(str(int(time.time())))  # getTime 当前时间的时间戳
        print(str(int(time.time())))
        m = t[0].find_all('td')
        a.append(m[1].string)  # zlm 专利名
        m = t[1].find_all('td')
        a.append(m[1].string)  # sqh 申请号
        a.append(m[3].string)  # sqDate 申请日期
        m = t[2].find_all('td')
        a.append(m[1].string)  # gbh 公布号
        a.append(m[3].string)  # gbDate 公布日期
        m = t[3].find_all('td')
        a.append(m[1].string)  # fmPerson 发明人
        a.append(m[3].string)  # zlsqPerson 专利申请人
        m = t[4].find_all('td')
        a.append(m[1].string)  # zldlPerson 专利代理人
        a.append(m[3].string)  # zlAgency 专利代理机构
        m = t[5].find_all('td')
        a.append(m[1].string)  # zlCategory 专利类型
        a.append(m[3].string)  # flNumber 主分类号
        m = t[6].find_all("td")
        a.append(m[1].string)     # 地址'address'
        m = t[7].find_all('td')
        a.append(m[1].string)  # flStatus 法律状态

        inDB(a)
        count += 1
        rate = count / 2082
        print('插入进度：' + str(rate))
        time.sleep(6)
    print('count------------------', count)