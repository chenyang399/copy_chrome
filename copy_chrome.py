import shutil
import os
import win32api
import win32con
import pyautogui
import time

# 等待时间，用于等待操作完成
WAIT_TIME = 3


def mod_destination_path(chrome_icon_position,number):
        # 模拟左击 Chrome 图标
        
    # left, top, width, height = pyautogui.locateOnScreen(icon_path)  # 寻找刚才保存点赞手势图片
    # chrome_icon_position = pyautogui.center((left, top, width, height))  # 寻找图片的中心
    # pyautogui.click(center)

    # chrome_icon_position = pyautogui.locateCenterOnScreen(icon_path)
    if chrome_icon_position is None:
        print("Chrome 图标未找到！")
        exit()
    
    pyautogui.click(chrome_icon_position)
    time.sleep(WAIT_TIME)
    
    # 模拟按下 Alt+Enter 打开文件属性
    pyautogui.hotkey('alt', 'enter')
    time.sleep(WAIT_TIME)
    
    # 模拟键盘右方向操作
    pyautogui.press('right')
    time.sleep(WAIT_TIME)
    
    # 模拟点击空格键
    pyautogui.press('space')
    time.sleep(WAIT_TIME)
    
    # 输入文本"--user-data-dir=D:chrome\\1"
    pyautogui.typewrite("--user-data-dir=D:chrome\\")
    pyautogui.press('space')
    pyautogui.typewrite(number)
    time.sleep(WAIT_TIME)
    
    # 模拟按下 Tab 键 8 次
    for _ in range(8):
        pyautogui.press('tab')
        # time.sleep(WAIT_TIME)
    
    # 模拟按下 Enter 键
    pyautogui.press('enter')



def open_all(chrome_icon_position):
    pyautogui.click(chrome_icon_position)
    pyautogui.click(chrome_icon_position)
    time.sleep(WAIT_TIME)
    
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(WAIT_TIME)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(WAIT_TIME)

    
    
    
    
# import sys  
# import io  

# # 设置标准输出的编码为 UTF-8  
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if __name__ == "__main__":
    # 源快捷方式路径
#    
    file_positions  = pyautogui.locateAllOnScreen("C:\\Users\\10611\\Desktop\\chrome_icon.png")  # 寻找刚才保存的图片
    
    i=109
    for file_position in file_positions:
        print("现在处理第" + str(i)+"个chrome")
        # open_all(pyautogui.center(file_position))
        mod_destination_path()
        i+=1
    
#     4  6
# cong  52  50