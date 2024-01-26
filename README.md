# miHoYoCloudGame
首个米家云游戏2合1的启动器
# 米哈云游启动器

**米哈云游启动器** 是首个米家云游戏2合1的启动器，由开发者 JackTao 创作。这款启动器使用 Python 语言编写，并遵循 GPL3.0 协议开源。

## 主要功能

- 提供简洁的用户界面，方便用户选择要启动的云游戏。
- 支持崩坏·星穹铁道和原神两款米家云游戏。
- 集成作者信息，并提供快速访问作者页面的功能。

## 源码解析

以下是米哈云游启动器的核心源码解析：


```python
import webview
import tkinter as tk
from tkinter import ttk

games = "https://mhyy.mihoyo.com/"

# 创建 Tkinter 主窗口
root = tk.Tk()
root.title("米哈云游")
root.geometry("300x200")
root.resizable(False, False)  # 禁止调整窗口大小

# 创建标签和按钮组
label = ttk.Label(root, text="请选择要启动的云游戏")
label.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# 定义按钮点击事件处理函数
def start_game1():
    global games
    games = "https://sr.mihoyo.com/cloud"
    close_window()

def start_game2():
    global games
    games = "https://ys.mihoyo.com/cloud"
    close_window()

def author_link():
    import webbrowser
    webbrowser.open("https://space.bilibili.com/1337924642")
    close_window()

def close_window():
    root.destroy()
    print("游戏已启动：", games)

# 创建按钮
button1 = ttk.Button(button_frame, text="崩坏·星穹铁道", command=start_game1)
button1.pack(side=tk.LEFT, padx=5, pady=5)

button2 = ttk.Button(button_frame, text="原神", command=start_game2)
button2.pack(side=tk.LEFT, padx=5, pady=5)

author_btn = ttk.Button(button_frame, text="关于作者", command=author_link)
author_btn.pack(side=tk.LEFT, padx=5, pady=5)

# 运行 Tkinter 主循环
root.mainloop()

# 使用 webview 创建游戏窗口
window = webview.create_window(
    title='米哈云游',
    url=games,
    width=1280,
    height=800,
    resizable=True,
    text_select=False,
    confirm_close=False
)

# 启动 webview 主循环
webview.start()
```
### 注意

- 源码中存在一个小错误，即 `root.mainloop()` 被调用了两次，这是不必要的。应该只保留一次调用。
- 为了使代码更加清晰和易于维护，建议将 Tkinter 界面和 webview 界面的创建逻辑进行分离，可以考虑使用面向对象的设计模式。

总体而言，米哈云游启动器是一个实用且开源的项目，为米家云游戏玩家提供了便利的启动方式。感谢 JackTao 的贡献！
