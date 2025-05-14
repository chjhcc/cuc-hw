import tkinter as tk

def read_info():
    work = entry_work.get()
    author = entry_author.get()
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, f"作品：{work}作者：{author}")

def exit_program():
    window.destroy()

window = tk.Tk()
window.title("作品信息")

label_work = tk.Label(window, text="作品：",fg = "blue")
label_work.grid(row=0, column=0)
entry_work = tk.Entry(window)
entry_work.grid(row=0, column=1)

label_author = tk.Label(window, text="作者：",fg = "red")
label_author.grid(row=1, column=0)
entry_author = tk.Entry(window)
entry_author.grid(row=1, column=1)

button_read = tk.Button(window, text="读取信息", command=read_info)
button_read.grid(row=2, column=0)

text_result = tk.Text(window, width=30, height=5)
text_result.grid(row=3, column=0, columnspan=2)

button_exit = tk.Button(window, text="退出", command=exit_program)
button_exit.grid(row=4, column=0, columnspan=2)

window.mainloop()

label_author.grid(row=1, column=0)
entry_author = tk.Entry(window)
entry_author.grid(row=1, column=1)

button_read = tk.Button(window, text="读取信息", command=read_info)
button_read.grid(row=2, column=0)

text_result = tk.Text(window, width=30, height=5)
text_result.grid(row=3, column=0, columnspan=2)

button_exit = tk.Button(window, text="退出", command=exit_program)
button_exit.grid(row=4, column=0, columnspan=2)

window.mainloop()
