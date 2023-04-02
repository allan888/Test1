import threading
import tkinter as tk
import random
from tkinter import ttk
import time
import pyttsx3
from tkinter import  messagebox as msgbox
import os
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 1)
person = []
running_flag = False
width = 406
height = 229
root = tk.Tk()
a = tk.StringVar()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(size_geo)
root.title("差距已经拉开了")
root.iconbitmap("./resources/ico.ico")
root.tk.call("source", "./resources/sun-valley.tcl")
root.tk.call("set_theme", "light")
style_default = ttk.Style()
style_default.configure("myname.TButton", font="站酷文艺体")
style_default.configure("myname.TLabel", foreground="#FFD4A9", background="#80D1C8")


def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


def start():
    if os.path.isfile('person.txt'):
        with open('person.txt', encoding='utf-8') as f:
            for line in f.readlines():
                person.append(line.strip('\n').split(',')[0])

        number = len(person)
    else:
        msgbox.showerror("错误", "未找到person.txt")
        file = open('person.txt', 'w')
        file.close()
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


def stop():
    global running_flag
    if running_flag:
        running_flag = False
        time.sleep(1)
        s1 = "恭喜"
        s2 = "同学被抽到"
        engine.say(s1+a.get()+s2)
        engine.runAndWait()
        engine.stop()

def stop_time():
    timer = threading.Timer(3, stop)
    timer.start()


a.set("?")
l2 = ttk.Label(root, textvariable=a, font=("站酷文艺体", 50), style="myname.TLabel", anchor="center", relief="sunken")
l2.place(x=9, y=10, width=384, height=104)
button = ttk.Button(root, text="摸一个", command=lambda: thread_it(start), style="myname.TButton")
button.place(x=145, y=133, width=100, height=48)
# ttk.Button(root, text="stop", command=stop, style="myname.TButton").place(x=200, y=133, width=100, height=48)

root.mainloop()
