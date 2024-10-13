import pyautogui
from pynput import keyboard


def on_press(key):
    if key == keyboard.KeyCode(char='p'):  # 如果按下的是'p'键
        print('你按下了"p"键！')
        print("即将开始工作")
        pyautogui.moveTo(10, 10, duration=0)  # duration参数可选，表示移动所需的时间（秒）
        pyautogui.click() # 执行鼠标点击
        pyautogui.click() # 执行鼠标点击
        pyautogui.moveTo(300, 70, duration=0)
        pyautogui.click()
        pyautogui.typewrite('github.com')
        pyautogui.press('enter')
        pyautogui.press('enter')
        print("打开git")

        
# 使用Listener来监听键盘事件
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
