from tkinter import *
import math

window = Tk()
window.title('SCIENTIFIC CALCULATOR')


class Calculator:
    def __init__(self, master):
        self.master = master

        # Create entry widget for input and output

        self.entry = Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Create buttons for calculator functions
        self.button_1 = Button(master, text="7", padx=30, pady=20, command=lambda: self.button_click)
        self.button_2 = Button(master, text="8", padx=30, pady=20, command=lambda: self.button_click)
        self.button_3 = Button(master, text="9", padx=30, pady=20, command=lambda: self.button_click)
        self.button_4 = Button(master, text="/", padx=27, pady=20, command=lambda: self.button_click)
        self.button_5 = Button(master, text="4", padx=22, pady=20, command=lambda: self.button_click)
        self.button_6 = Button(master, text="5", padx=30, pady=20, command=lambda: self.button_click)
        self.button_7 = Button(master, text="6", padx=30, pady=20, command=lambda: self.button_click)
        self.button_8 = Button(master, text="*", padx=30, pady=20, command=lambda: self.button_click)
        self.button_9 = Button(master, text="1", padx=30, pady=20, command=lambda: self.button_click)
        self.button_10 = Button(master, text="2", padx=27, pady=20, command=lambda: self.button_click)
        self.button_11 = Button(master, text="3", padx=22, pady=20, command=lambda: self.button_click)
        self.button_12 = Button(master, text=")", padx=30, pady=20, command=lambda: self.button_click)
        self.button_13 = Button(master, text="0", padx=30, pady=20, command=lambda: self.button_click)
        self.button_14 = Button(master, text=".", padx=30, pady=20, command=lambda: self.button_click)
        self.button_15 = Button(master, text="pi", padx=30, pady=20, command=lambda: self.button_click)
        self.button_16 = Button(master, text=")", padx=27, pady=20, command=lambda: self.button_click)
        self.button_17 = Button(master, text="+", padx=22, pady=20, command=lambda: self.button_click)
        self.button_18 = Button(master, text="-", padx=30, pady=20, command=lambda: self.button_click)
        self.button_sin = Button(master, text="sin", padx=30, pady=20, command=lambda: self.button_click(math.sin))
        self.button_cos = Button(master, text="cos", padx=30, pady=20, command=lambda: self.button_click(math.cos))
        self.button_tan = Button(master, text="tan", padx=30, pady=20, command=lambda: self.button_click(math.tan))
        self.button_sqrt = Button(master, text="sqrt", padx=27, pady=20, command=lambda: self.button_click(math.sqrt))
        self.button_clear = Button(master, text="Clear", padx=22, pady=20, command=self.clear)
        self.button_equals = Button(master, text="=", padx=30, pady=20, command=self.calculate)

        # Position the buttons on the GUI

        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.button_4.grid(row=1, column=3)
        self.button_5.grid(row=2, column=0)
        self.button_6.grid(row=2, column=1)
        self.button_7.grid(row=2, column=2)
        self.button_8.grid(row=2, column=3)
        self.button_9.grid(row=3, column=0)
        self.button_10.grid(row=3, column=1)
        self.button_11.grid(row=3, column=2)
        self.button_12.grid(row=3, column=3)
        self.button_13.grid(row=4, column=0)
        self.button_14.grid(row=4, column=1)
        self.button_15.grid(row=4, column=2)
        self.button_16.grid(row=4, column=3)
        self.button_17.grid(row=5, column=0)
        self.button_18.grid(row=5, column=1)
        self.button_sin.grid(row=5, column=2)
        self.button_cos.grid(row=5, column=3)
        self.button_tan.grid(row=6, column=0)
        self.button_sqrt.grid(row=6, column=1)
        self.button_clear.grid(row=6, column=2)
        self.button_equals.grid(row=6, column=3)

    def create_button(self, text, row, column):
        button = Button(self.master, text=text, padx=30, pady=20,
                        command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == '=':
            result = self.calculate()
            self.entry.delete(0, END)
            self.entry.insert(0, result)
        elif text == 'C':
            self.entry.delete(0, END)

        elif text in ('sin', 'cos', 'tan'):
            result = getattr(math, text)(float(self.entry.get()))
            self.entry.delete(0, END)
            self.entry.insert(0, result)
        else:
            self.entry.insert(END, text)

    def clear(self):
        self.entry.delete(0, END)

    def calculate(self):
        try:
            result = eval(self.entry.get())
        except:
            result = 'Error'
        return result


root = Tk()
calc = Calculator(root)
root.mainloop()
