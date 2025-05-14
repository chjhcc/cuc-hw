import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("科学计算器")
        self.geometry("400x600")
        self.create_widgets()

    def create_widgets(self):
        # 定义所有按钮的标签和命令
        buttons = [
            ('7', 'button_7'),
            ('8', 'button_8'),
            ('9', 'button_9'),
            ('+', 'button_add'),
            ('4', 'button_4'),
            ('5', 'button_5'),
            ('6', 'button_6'),
            ('-', 'button_subtract'),
            ('1', 'button_1'),
            ('2', 'button_2'),
            ('3', 'button_3'),
            ('*', 'button_multiply'),
            ('0', 'button_0'),
            ('.', 'button_dot'),
            ('=', 'button_equal'),
            ('/', 'button_divide')
        ]
        # 创建一个网格布局来放置所有的按钮
        for i in range(5):
            for j in range(4):
                if (i, j) == (2, 3):  # 将等号放在中间行和中间列上
                    continue
                w = tk.Button(self, text=buttons[i][j], command=lambda button=buttons[i][j]: self.button_press(button))
                w.grid(row=i, column=j)
        # 添加一个函数来处理按钮点击事件
        self.bind("<Button-1>", lambda event: self.button_press("backspace"))
        self.bind("<Return>", self.calculate)
        self.bind("<Escape>", self.cancel)
        self.mainloop()

    def button_press(self, button):
        # 处理按钮点击事件的逻辑
        pass

    def calculate(self):
        try:
            expression = str(self.display_entry.get()) + "=" + str(self.result_entry.get())
            result = eval(expression)  # 使用eval函数进行计算，但请注意，这可能会有安全风险！
            self.result_entry.set(result)
        except Exception as e:
            self.result_entry.set("错误")

    def cancel(self):
        self.display_entry.set("")  # 清除输入栏的内容当用户按下Esc键时。
        self.result_entry.set("")  # 清除结果栏的内容当用户按下Esc键时。

if __name__ == '__main__':
    calculator = Calculator()
