import tkinter as tk
from tkinter import messagebox


def check_login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "123456":
        messagebox.showinfo("登录成功", "欢迎进入游戏！")
        window.destroy()
    else:
        messagebox.showerror("错误", "用户名或密码错误")

window = tk.Tk()
window.title("登录界面")

label_username = tk.Label(window, text="用户名：")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(window)
entry_username.grid(row=0, column=1)

label_password = tk.Label(window, text="密码：")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(window, show="*")
entry_password.grid(row=1, column=1)

button_login = tk.Button(window, text="进入游戏", command=check_login)
button_login.grid(row=2, column=0, columnspan=2)

window.mainloop()
