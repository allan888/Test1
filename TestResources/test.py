import tkinter as tk
import win32gui
import win32con
import subprocess
import time
import os
import threading

running_flag = True


def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


def treat(root):
    a = win32gui.FindWindow(None, "差距已经拉开了")
    left, top, right, bottom = win32gui.GetWindowRect(a)
    AppX = right - left
    AppY = bottom - top
    TargetX = int((screenwidth - AppX + 1) / 2)
    TargetY = int((screenheight - AppY + 1) / 2)
    TrueY = TargetY + AppY
    for i in range(0, TrueY):
        win32gui.MoveWindow(a, TargetX, TargetY + i, AppX, AppY, True)
        time.sleep(0.00001)
    root.withdraw()


root = tk.Tk()
root.title("差距已经拉开了")
width = 406
height = 229
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(size_geo)


def action():
    thread_it(treat(root))


# subprocess.Popen('C:\windows\system32\cmd.exe')
# a = win32gui.FindWindow('ConsoleWindowClass', None)
root.protocol('WM_DELETE_WINDOW', action)
root.mainloop()
