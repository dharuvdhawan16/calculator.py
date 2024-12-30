from tkinter import *
from tkinter import ttk
import math

def calculate(event=None):
    expression = show_entery.get()
    try:
        result = eval(expression)
        show_entery.delete(0, END)
        show_entery.insert(END, str(result))
    except Exception as e:
        show_entery.delete(0, END)
        show_entery.insert(END, "Error")

def add_number_to_entry(number):
    current_text = show_entery.get()
    show_entery.delete(0, END)
    show_entery.insert(END, current_text + str(number))

def enter_num(num):
    show_entery.delete(0, END)
    show_entery.insert(END, str(num))

root = Tk()
root.title("Calculator")
root.attributes("-topmost", True)
root.geometry("235x230")

mainframe = ttk.Frame(root, padding="3 9 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

show_entery = ttk.Entry(mainframe, width=20)
show_entery.grid(column=0, row=0, columnspan=4, sticky=(W, E), pady=5)

# Buttons for numbers
for i in range(1, 10):
    ttk.Button(mainframe, text=str(i), command=lambda i=i: add_number_to_entry(i)).grid(
        column=(i - 1) % 3, row=(i - 1) // 3 + 1, sticky=(N, S, E, W), pady=5, padx=5
    )

# Special buttons
special_buttons = {
    "0": 0,
    "sqrt": "sqrt",
    "ceil": "ceil",
    "+": "+",
    "-": "-",
    "x": "*",
    "/": "/",
    "pow": "**",
    "log": "math.log10",
    "enter": calculate,
    "calculate": calculate,
}

row_num = 4
col_num = 0
for button_text, command in special_buttons.items():
    ttk.Button(mainframe, text=button_text, command=lambda command=command: add_number_to_entry(command) if isinstance(command, int) else command()).grid(
        column=col_num, row=row_num, sticky=(N, S, E, W), pady=5, padx=5
    )
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1

# Run the Tkinter event loop
root.mainloop()
