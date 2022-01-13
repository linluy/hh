import tkinter as tk
from tkinter import scrolledtext
import socket
import threading
from datetime import datetime


def tcp_recv(sock):
    while True:
        str = sock.recv(1024).decode("utf-8")
        show_info(str)


# 得到待发消息，发送消息
def send_func(sock):
    str = send_msg.get("0.0", "end")  # 得到待发消息页面输入的内容
    sock.send(str.encode("utf-8"))  # 服务器端发送消息
    show_info(str)


#
def show_info(str):
    now = datetime.now()  # 消息发送时间
    s_time = now.strftime("%Y-%m-%d %H:%M:%S")  # 规范化
    str = str.rstrip()  # 删除 string 字符串末尾的指定字符(默认为空格).
    if len(str) == 0:
        return -1
    send_msg.delete("0.0", "end")
    temp = s_time + "\n    " + str + "\n"
    show_msg.insert(tk.INSERT, "%s" % temp)


msFont = '微软雅黑'  # 字体
fontSize = 15  # 字体大小
# 创建一个socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定socket
sock.bind(("127.0.0.1", 8888))
# 服务器端开始监听
sock.listen(5)

# 创建Tkinter窗口
mainWindow = tk.Tk()  # 初始化TK()
mainWindow.title("服务器")  # 给窗口设置一个标题
mainWindow.minsize(400, 400)  # 设置Tkinter窗口的最小大小
show_msg = scrolledtext.ScrolledText(mainWindow, font=(msFont, fontSize))  # 已发送消息的页面，可以设置宽，高以及字体样式
show_msg.place(width=400, height=250, x=0, y=0)  # 宽度和高度，以及在窗口的位置
send_msg = scrolledtext.ScrolledText(mainWindow, font=(msFont, fontSize))  # 待发消息的页面，可以设置宽，高以及字体样式
send_msg.place(width=400, height=140, x=0, y=260)  # 设置待发消息的页面，其中y固定了此窗口的位置
button_send = tk.Button(mainWindow, font=(msFont, fontSize), text="发  送", bg="Pink", fg="white",
                        command=lambda: send_func(s))  # command指定button的事件处理器，使用lambda匿名函数
button_send.place(width=100, height=40, x=300, y=360)  # x和y固定了按钮在窗口的位置，再设计按钮的宽和高

s, addr = sock.accept()
t = threading.Thread(target=tcp_recv, args=(s,))
t.start()
tk.mainloop()
