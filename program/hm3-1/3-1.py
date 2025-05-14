import tkinter as tk							#导入tkinter模块重命名为tk
#定义函数，用于实现改变标签的内容
def btnHelloClicked():
    labelHello.config(text="欢迎进入飞机大战游戏!")
top = tk.Tk()								#创建tkinter对象
top.geometry("200x150")					#设置窗口的大小，注意是字母x
top.title("Button Test")						#设置窗口标题
#创建原始标签
labelHello = tk.Label(top, text="Press the button...", height = 5, width = 20, fg = "blue")
labelHello.pack()							#显示标签
#创建按钮，显示“Hello”，单击按钮调用btnHelloClicked函数
btn = tk.Button(top, text = "Click", command=btnHelloClicked)
btn.pack()								#显示按钮
top.mainloop()								#进入主事件循环