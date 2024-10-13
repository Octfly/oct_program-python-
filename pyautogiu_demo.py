import pyautogui
from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.esc:
        print("end")  # 如果按下的是Esc键，则停止监听
        return False
    if key == keyboard.KeyCode(char='a'):  # 如果按下的是'a'键
        print('你按下了"a"键！')
        print("即将开始工作")
        pyautogui.moveTo(2400, 30, duration=0)  # duration参数可选，表示移动所需的时间（秒）
        pyautogui.click() # 执行鼠标点击
        pyautogui.moveTo(1500, 1570, duration=0)  # duration参数可选，表示移动所需的时间（秒）
        pyautogui.click() # 执行鼠标点击
        print("把全屏的IDE窗口切换到最小化，然后再打开")
    if key == keyboard.KeyCode(char='p'):  # 如果按下的是'p'键
        print('你按下了"p"键！')
        print("即将开始工作")
        pyautogui.moveTo(10, 10, duration=0)  # duration参数可选，表示移动所需的时间（秒）
        pyautogui.click() # 执行鼠标点击
        pyautogui.click() # 执行鼠标点击
        print("打开桌面第一个程序")

        
# 使用Listener来监听键盘事件
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
