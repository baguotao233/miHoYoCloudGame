import webview
import tkinter as tk  
from tkinter import ttk  

import platform

games = "https://mhyy.mihoyo.com/" 
# 创建主窗口  
root = tk.Tk()  
root.title("米哈云游")  

# select system
systemPlatform = platform.system()
if systemPlatform == "Windows":
    root.geometry("300x200")  
elif systemPlatform == "Darwin":
    root.geometry("350x100")  

root.resizable(False, False)  # 禁止调整窗口大小  
# 创建标签  
label = ttk.Label(root, text="请选择要启动的云游戏")  
label.pack(pady=10)  
# 创建按钮组  
button_frame = ttk.Frame(root)  
button_frame.pack(pady=10)  
  
# 创建按钮并绑定函数  
def start_game1():  
    global games  
    games = "https://sr.mihoyo.com/cloud"  
    close_window()  
    jumpWeb(games)
  
def start_game2():  
    global games  
    games = "https://ys.mihoyo.com/cloud"  
    close_window()  
    jumpWeb(games)
  
def author_link():  # 点击后跳转网址到作者页面  
    import webbrowser  
    webbrowser.open("https://space.bilibili.com/1337924642")  # 跳转到作者页面  
    close_window()  # 关闭窗口并继续执行下面的代码  
  
def close_window():  # 关闭窗口并继续执行下面的代码  
    root.destroy()  
    print("游戏已启动：", games)  # 这里可以替换为你的其他代码逻辑  
  
# 创建按钮和标签文本  
button1 = ttk.Button(button_frame, text="崩坏·星穹铁道", command=start_game1)  
button1.pack(side=tk.LEFT, padx=5, pady=5)  
button2 = ttk.Button(button_frame, text="原神", command=start_game2)  
button2.pack(side=tk.LEFT, padx=5, pady=5)  
author_btn = ttk.Button(button_frame, text="关于作者", command=author_link)  # 新增按钮关于作者，点击后跳转网址到作者页面  
author_btn.pack(side=tk.LEFT, padx=5, pady=5)  
label_text = ttk.Label(root, text="")  
label_text.pack(pady=10)  


def jumpWeb(game):
    window = webview.create_window(
        title='米哈云游',
        url=games,
        width=1280,
        height=800,
        resizable=True,    # 固定窗口大小
        text_select=False,   # 禁止选择文字内容
        confirm_close=False   # 关闭时提示
    )
    webview.start()


# 运行主循环  
root.mainloop()
