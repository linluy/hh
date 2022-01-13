# print('hello')
# -*- coding: utf-8 -*-
from typing import List, Any

import requests
import json
import time
import csv
import codecs
import pandas as pd
from matplotlib import pyplot as plt
import math

file_load = 'D:/Program Files (x86)/soft_runResult/weather.csv'


def get_data(city):            # 获取数据
    p = {"city": city}
    url = "http://wthrcdn.etouch.cn/weather_mini"
    r = requests.get(url, p)
    r.encoding = "utf-8"
    return r.text


def save_data(list, name):       # 生成csv文件
    weatherData = pd.DataFrame(columns=name, data=list)
    weatherData.to_csv(file_load, encoding='gbk')


def deal_data(data):                                        # 获取yesterday以及forecast的日期、最高温度、
    data_list = []
    yesterday_info = data['yesterday']                      # 获取昨天的天气信息
    forecast_info = data['forecast']                        # 获取今天及以后的天气信息
    dates = yesterday_info['date']
    highs = yesterday_info['high']
    lows = yesterday_info['low']
    data_one = [dates, highs, lows]
    data_list.append(data_one)
    # print("data_one:%s" % data_one)
    for i in forecast_info:
        dates = i.get('date')
        highs = i.get('high')
        lows = i.get('low')
        data_one = [dates, highs, lows]
        data_list.append(data_one)
    return data_list


def create_graph():
    weather_date = []
    weather_max = []
    weather_min = []
    with codecs.open(file_load, 'rb', 'gb2312') as cs:
        read = csv.reader(cs)
        header = next(read)                     # next()函数返回文件的下一行，这里只调用一次就返回第一行，同时因为对read调用了一次next，所以之后的read读取会从第二行开始
        row = 0

        for i in read:
            # i[2] = filter(str.isdigit, i[2])
            i[2] = "".join(list(filter(str.isdigit,  i[2])))
            i[3] = "".join(list(filter(str.isdigit,  i[3])))
            # i[3] = filter(str.isdigit, i[3])
            weather_date.append((i[1]))  # 提取csv文件里面的第一列数据
            weather_max.append((int)(i[2]))  # 提取csv文件里面的第二列数据
            weather_min.append((int)(i[3]))  # 提取csv文件里面的第三列数据
    plt.plot(weather_date, weather_max, c='yellow')
    plt.plot(weather_date, weather_min, c='red')
    plt.show()


if __name__ == '__main__':
    city = input()
    rt = get_data(city)
    data_json = json.loads(rt)
    data = data_json['data']
    name = ['date', 'high', 'low']                       # 表名
    data_list = deal_data(data)
    save_data(data_list, name)
    create_graph()


