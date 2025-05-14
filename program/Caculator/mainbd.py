import tkinter as tk
from math import pi, e, sin, cos, tan, log, exp, factorial

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("计算器")
        self.geometry("400x600")
        self.create_widgets()

    def create_widgets(self):
        # 创建标签
        self.label = tk.Label(self, text="0", anchor=tk.E, font=("Arial", 24), bg="white", bd=10)
        self.label.pack(fill=tk.BOTH, expand=True)

        # 创建数字按钮
        for i in range(9, 0, -3):
            for j in range(i, i - 3, -1):
                button = tk.Button(self, text=str(j), font=("Arial", 18), command=lambda j=j: self.on_click(j))
                button.place(x=(i % 3) * 80 + 10, y=(2 - i // 3) * 80 + 50)

        # 创建小数点、负号、加号等按钮
        buttons = [(".", "decimal"), ("-", "minus"), ("+", "plus"), ("(", "lparen"), (")", "rparen"), ("{", "lbrace"), ("}", "rbrace"), ("[", "lbracket"), ("]", "rbracket")]
        for i, (text, command) in enumerate(buttons):
            button = tk.Button(self, text=text, font=("Arial", 18), command=lambda command=command: self.on_click(command))
            button.place(x=(i % 4) * 80 + 10, y=500)

        # 创建等于号、清除键、退格键等按钮
        buttons = [("=", "equal"), ("C", "clear"), ("Backspace", "backspace")]
        for i, (text, command) in enumerate(buttons):
            button = tk.Button(self, text=text, font=("Arial", 18), command=lambda command=command: self.on_click(command))
            button.place(x=(i % 3) * 80 + 240, y=500)

    def on_click(self, value):
        # 在这里处理按钮点击事件
        pass

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
