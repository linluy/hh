# print('hello')
# -*- coding: utf-8 -*-
from typing import List, Any

import requests
import json
import time
import datetime
import csv
import codecs
import pandas as pd
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

file_load = 'D:/Program Files (x86)/soft_runResult/weather.csv'
now_time = datetime.datetime.now()
now_year = now_time.year
now_month = now_time.month
now_day = now_time.day
dates = []


# 获取数据
def get_data(city):
    p = {"city": city}
    url = "http://wthrcdn.etouch.cn/weather_mini"
    r = requests.get(url, p)
    r.encoding = "utf-8"
    return r.text


# 生成csv文件
def save_data(list, name):
    weatherData = pd.DataFrame(columns=name, data=list)
    weatherData.to_csv(file_load, encoding='gbk')


# 得到最高温度、最低温度以及日期（包括从昨天开始的六天的天气）
def deal_data(data):
    data_list = []
    yesterday_info = data['yesterday']
    forecast_info = data['forecast']
    weather_date = yesterday_info['date']
    highs = yesterday_info['high']
    lows = yesterday_info['low']
    data_one = [weather_date, highs, lows]
    data_list.append(data_one)
    for i in forecast_info:
        # print("数据：%s   值：%s" % (forecast_info.index(i) + 1, i))
        weather_date = i.get('date')
        highs = i.get('high')
        lows = i.get('low')
        data_one = [weather_date, highs, lows]
        data_list.append(data_one)
    return data_list


# 生成图表
def create_graph():
    flag = 0  # 当flag = 0 时，表示昨天所在的月份，判断是不是需要进入下一个月以及年
    count = 0
    weather_date = []
    weather_max = []
    weather_min = []
    with codecs.open(file_load, 'rb', 'gb2312') as cs:
        read = csv.reader(cs)
        header = next(read)  # next()函数返回文件的下一行，这里只调用一次就返回第一行，同时因为对read调用了一次next，所以之后的read读取会从第二行开始
        row = 0
        for i in read:
            day_old = int("".join(list(filter(str.isdigit, i[1]))))
            if day_old == 1 and count != 0:
                new_year = now_year
                new_month = now_month + 1
                flag = 1
            elif flag == 0:
                new_year = now_year
                new_month = now_month
                count += 1
            elif flag == 1:
                new_year = now_year + 1
                new_month = now_month + 1
                count += 1
            i[1] = str(new_year) + '-' + str(new_month) + '-' + "".join(list(filter(str.isdigit, i[1])))
            i[2] = "".join(list(filter(str.isdigit, i[2])))
            temp = "".join(list(filter(str.isdigit, i[3])))
            if i[3].find("-", 0) >= 0:
                i[3] = '-' + temp
            else:
                i[3] = temp
            weather_date.append((i[1]))  # 提取csv文件里面的第一列数据
            weather_max.append(int(i[2]))  # 提取csv文件里面的第二列数据
            weather_min.append(int(i[3]))  # 提取csv文件里面的第三列数据

    starttime = datetime.datetime(*map(int, weather_date[0].split('-')))
    year = int(weather_date[len(weather_date)-1].split("-")[0])
    month = int(weather_date[len(weather_date)-1].split("-")[1])
    day = int(weather_date[len(weather_date)-1].split("-")[2]) + 1
    print("day: %s" % day)
    endtime = datetime.datetime(int(year),int(month),int(day))
    print("weather_date[len(weather_date)-1]:%s" % weather_date[len(weather_date)-1])
    interval = datetime.timedelta(days=1)
    dates = mpl.dates.drange(starttime, endtime, interval)
    fig = plt.figure(dpi=60, figsize=(24, 10))
    ax = fig.add_subplot(111)
    # dates = dates[:len(weather_min)]
    print("starttime: %s" % starttime)
    print("endtime: %s" % endtime)
    print("weather_min: %s" % weather_min)
    print("weather_max: %s" % weather_max)
    ax.plot_date(dates, weather_min, 'o-', label='最低气温', linewidth=5, markersize=15)
    for x, y in zip(dates, weather_min):
        plt.text(x, y, str(y) + "℃", fontsize=20)
    ax.plot_date(dates, weather_max, 'o-', color='grey', label='最高气温', linewidth=5, markersize=15)
    for x, y in zip(dates, weather_max):
        plt.text(x, y, str(y) + "℃", fontsize=20)
    plt.fill_between(dates, weather_max, weather_min, facecolor='blue', alpha=0.2)
    fig.autofmt_xdate()
    plt.legend()
    plt.title('6日天气气温状况', fontsize=30)
    plt.xlabel('日期', fontsize=30)
    plt.ylabel('温度', fontsize=30)
    plt.tick_params(labelsize=20)
    mpl.rcParams["font.sans-serif"] = ["KaiTi"]  # 以下两句防止中文乱码
    mpl.rcParams["axes.unicode_minus"] = False
    # plt.plot(weather_date, weather_max, c='yellow')
    # plt.plot(weather_date, weather_min, c='red')
    plt.show()


if __name__ == '__main__':
    city = input()
    rt = get_data(city)
    data_json = json.loads(rt)
    # print(data_json)
    data = data_json['data']
    # print("data:%s" % data)
    name = ['date', 'high', 'low']  # 表名
    data_list = deal_data(data)
    print("data_list:%s" % data_list)
    save_data(data_list, name)
    create_graph()
