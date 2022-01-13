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
    str = send_msg.get("0.0", "end")  # 这个地方不大理解
    sock.send(str.encode("utf-8"))
    show_info(str)


def show_info(str):
    now = datetime.now()
    s_time = now.strftime("%Y-%m-%d %H:%M:%S")
    str = str.rstrip()  # 去掉空结尾格     str.lstrip()  删除开头空格
    if len(str) == 0:
        return -1
    send_msg.delete("0.0", "end")
    temp = s_time + "\n    " + str + "\n"
    show_msg.insert(tk.INSERT, "%s" % temp)


# 和服务器端一样的窗口
msFont = '微软雅黑'  # 字体
fontSize = 18  # 字体大小
# 创建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 客户端进行连接，端口号是8888
sock.connect(("127.0.0.1", 8888))

mainWindow = tk.Tk()
mainWindow.title("客户端")
mainWindow.minsize(400, 400)
show_msg = scrolledtext.ScrolledText(mainWindow, font=(msFont, fontSize))
show_msg.place(width=400, height=250, x=0, y=0)
# show_msg.insert(tk.INSERT,"%s 已连接\n"%addr[0])
send_msg = scrolledtext.ScrolledText(mainWindow, font=(msFont, fontSize))
send_msg.place(width=400, height=140, x=0, y=260)
button_send = tk.Button(mainWindow, font=(msFont, fontSize), text="发  送", bg="PowDerBlue", fg="white",
                        command=lambda: send_func(sock))
button_send.place(width=100, height=40, x=300, y=360)

# 创建一个线程
t = threading.Thread(target=tcp_recv, args=(sock,))
# 开启线程
t.start()
# 接收操作系统发来的事件，然后把事件分发给各个控件和窗体
tk.mainloop()
