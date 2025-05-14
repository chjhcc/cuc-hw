import tkinter as tk
import math


class Calculator():
    def __init__(self, master):
        self.master = master
        master.title("Basic Calculator")

        # 创建计算器显示屏
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # 创建按钮
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)
        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2)
        self.create_button('+', 4, 3)
        self.create_button('=', 5, 1, 2)
        self.create_button('切换', 5, 0,2)

    def create_button(self, text, row, col, colspan=1):
        button = tk.Button(self.master, text=text, width=5, command=lambda: self.button_click(text))
        button.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)

    def button_click(self, text):
        if text == 'C':
            self.display.delete(0, tk.END)
        elif text == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == '切换':
            AdvancedCalculator(root)
        elif text == '反三角函数':
            AnotherAdvancedCalculator(root)
        elif text == '基本':
            Calculator(root)
        else:
            self.display.insert(tk.END, text)

class AdvancedCalculator(Calculator):
    def __init__(self, master):
        super().__init__(master)
        # 创建高级计算器特有的按钮
        self.create_button('sin', 1, 4)
        self.create_button('cos', 2, 4)
        self.create_button('tan', 3, 4)
        self.create_button('log', 4, 4)
        self.create_button('ln', 5, 4)
        self.create_button('pi', 5, 3)
        self.create_button('反三角函数', 5, 0, 2)

    def create_button(self, text, row, col, colspan=1):
        if text in ['sin', 'cos', 'tan', 'log', 'ln']:
            button = tk.Button(self.master, text=text, width=5, command=lambda: self.special_button_click(text))
        else:
            button = tk.Button(self.master, text=text, width=5, command=lambda: self.button_click(text))
        button.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)

    def special_button_click(self, text):
        if text == 'sin':
            try:
                result = math.sin(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'cos':
            try:
                result = math.cos(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'tan':
            try:
                result = math.tan(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'log':
            try:
                result = math.log10(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'ln':
            try:
                result = math.log(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'pi':
            self.display.insert(tk.END, str(math.pi))


class AnotherAdvancedCalculator(Calculator):
    def __init__(self, master):
        super().__init__(master)
        # 创建高级计算器特有的按钮
        self.create_button('asin', 1, 4)
        self.create_button('acos', 2, 4)
        self.create_button('atan', 3, 4)
        self.create_button('log', 4, 4)
        self.create_button('ln', 5, 4)
        self.create_button('pi', 5, 3)
        self.create_button('基本', 5, 0, 2)

    def create_button(self, text, row, col, colspan=1):
        if text in ['asin', 'acos', 'atan', 'log', 'ln']:
            button = tk.Button(self.master, text=text, width=5, command=lambda: self.special_button_click(text))
        else:
            button = tk.Button(self.master, text=text, width=5, command=lambda: self.button_click(text))
        button.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)

    def special_button_click(self, text):
        if text == 'asin':
            try:
                result = math.asin(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'acos':
            try:
                result = math.acos(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'atan':
            try:
                result = math.atan(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'log':
            try:
                result = math.log10(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'ln':
            try:
                result = math.log(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == 'pi':
            self.display.insert(tk.END, str(math.pi))

root = tk.Tk()
advanced_calc = AdvancedCalculator(root)
root.mainloop()