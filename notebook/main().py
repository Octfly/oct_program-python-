import def_file
from pynput import keyboard

while True:
    def_file.u2()
    if def_file.u == "load":
        def_file.load()
        print("已读取")
    elif def_file.u == "quit":
        print("已退出")
        break
    else:
        def_file.save()