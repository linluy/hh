import csv
import requests
import bs4
import time

# 写csv文件
if __name__ == '__main__':
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Connection': 'keep-alive',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer': 'https://aiqicha.baidu.com/company_detail_13100503229410?tab=certRecord'
    }

    rids = []
    with open("s.csv", "r", encoding="utf_8_sig", newline="") as cr:
        d = csv.reader(cr, delimiter=',')
        for r in d:
            rids.append(r[1])
    el = []
    # print(d)
    title = ['zlm', 'sqh', 'sqrq', 'gbh', 'gbrq', 'fmr', 'sqr', 'dlr', 'dljg', 'fmlx', 'zflh', 'flzt', 'zy']
    with open("d.csv", "w+", encoding="utf_8_sig", newline="") as cf:
        wr = csv.writer(cf)
        wr.writerow(title)
        x = 1
        y = 0
        for rid in rids[1:]:
            print("Rid:", rid, end='')
            try:
                u = "https://www.baidu.com/"
                r = requests.get(url=u, headers=h)
                c = r.cookies
                u = "https://aiqicha.baidu.com/patent/info"
                p = {"referId": rid, "pid": "13100503229410"}
                r = requests.get(url=u, params=p, headers=h, cookies=c)
                s = bs4.BeautifulSoup(r.content.decode("utf-8"), "lxml")
                t = s.find_all('tr')
                a = []
                m = t[0].find_all('td')
                a.append(m[1].string)
                m = t[1].find_all('td')
                a.append(m[1].string)
                a.append(m[3].string)
                m = t[2].find_all('td')
                a.append(m[1].string)
                a.append(m[3].string)
                m = t[3].find_all('td')
                a.append(m[1].string)
                a.append(m[3].string)
                m = t[4].find_all('td')
                a.append(m[1].string)
                a.append(m[3].string)
                m = t[5].find_all('td')
                a.append(m[1].string)
                a.append(m[3].string)
                m = t[7].find_all('td')
                a.append(m[1].string)
                m = t[8].find_all('td')
                a.append(m[1].string)
                wr.writerow(a)
                time.sleep(1)
                y = y + 1
                if y >= 10:
                    time.sleep(20)
                    y = 1
            except Exception as e:
                x = x + 1
                print("... Error!")
                print(str(e))
                time.sleep(x)
                if x >= 10:
                    break
            else:
                print("... done!")
        print(el)

