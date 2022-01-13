import requests
from pyecharts.charts import Bar
from pyecharts import options as opts
import json
import csv
import numpy as np


# 创建一个列表存放所有省的名字

# 1.获取数据
def get_data(city):
    p = {'province': city}
    url = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list"
    r = requests.get(url, p)
    # print(r.text)
    d = json.loads(r.text)
    # print(type(d["data"])) #<class 'list'>
    return d["data"]


# 现在只要'confirm_add'就能分析那个省的人爱得病，

# 2.获取'confirm_add'的总人数
def all_num(d):
    num = 0
    for i in range(0, len(d)):
        n = d[i]['confirm_add']
        if n == '':
            num += 0
        else:
            num += int(n)
    # num += int(d[i]['confirm_add'])
    # print(type(num)) # <class 'int'>
    return num


# 3.存放省名数据，csv
def to_csv():
    # 创建一个列表存放所有省的名字
    province_name = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南',
                     '湖北', '湖南', '广东', '广西', '海南', '四川', '贵州', '陕西', '甘肃', '青海', '宁夏', '新疆', '云南', '西藏']
    # 创建一个空列表存放各省总人数
    province_person = []
    for name in province_name:
        d = get_data(name)
        s = all_num(d)
        province_person.append(s)

    # encoding='utf_8_sig' 不嗯呢个单独设置成utf-8 会出现
    with open("w.csv", "w", newline="", encoding='utf_8_sig') as cf:
        # 将数据存入csv文件
        csv_writer = csv.writer(cf)
        csv_writer.writerow(province_name)
        csv_writer.writerow(province_person)
        cf.close()


# to_csv()
'''
# # 4.各省人数存入csv
# def person_to_csv():
#     # 创建一个空列表存放各省总人数
#     province_person = []
#     province_name = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','四川','贵州','陕西','甘肃','青海','宁夏','新疆','云南','西藏']
#     for name in province_name:
#         d = get_data(name)
#         s = all_num(d)
#         province_person.append(s)
#     with open("w.csv", "w", newline="",encoding='utf-8') as cf:
#     # 将数据存入csv文件
#         csv_writer = csv.writer(cf)
#         csv_writer.writerow(province_person)
#         cf.close()
# person_to_csv()

'''


# 4.读取csv文件
def read_csv():
    # 使用numpy读取csv文件
    with open('w.csv', encoding='utf-8') as f:
        data = np.loadtxt(f, str, delimiter=',')
        # 输出前两行
        d = data[:2]
        p_name = d[0]
        p_num = d[1]
        # print(d[0]) # 各省名
        # print(d[1]) # 各省人数
        # print(type(d[0])) #<class 'numpy.ndarray'>
        return p_name, p_num


# # 5.图表生成
def to_bar():
    columns, data = read_csv()
    # 格式不对，要转换成list
    columns1 = list(columns)
    # print(type(columns1))
    # print(columns1)
    data1 = list(data)
    # print(data1)
    bar = (
        Bar()
            .add_xaxis(columns1)
            .add_yaxis("各省新增确诊总人数", data1)
            .set_global_opts(title_opts=opts.TitleOpts(title="全国各省疫情新增确诊汇总"))
    )
    bar.render()


if __name__ == '__main__':
    to_csv()
    read_csv()
    to_bar()
