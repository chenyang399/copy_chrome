# copy_chrome
多开浏览器批量操作
# 操作步骤
1. 使用ctrl-c ctrl-v将chrome浏览器图标进行复制，直到复制到你想要的数量为止(类似下图所示)
![](1.png)
2. 修改copy_chrome.py之中的参数，包括i和文件路径，替换成自己需要的
```

file_positions  = pyautogui.locateAllOnScreen("C:\\Users\\10611\\Desktop\\撸毛脚本\\复制chrome\\chrome_icon.png")  # 寻找刚才保存点赞手势图片
    
i=109
```
3. 复制完成之后运行代码
```python
python copy_chrome.py
```
即可使得每个chrome都是新创建的，不会继承原本的账号