import pyautogui

if __name__ == "__main__":
    # 等待用户点击
    input("请将鼠标移到你想要获取坐标的位置，然后按 Enter 键：")
    
    # 获取鼠标当前位置
    current_mouse_position = pyautogui.position()
    print("鼠标当前位置:", current_mouse_position)