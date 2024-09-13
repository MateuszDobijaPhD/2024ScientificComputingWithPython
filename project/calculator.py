import tkinter as tk
from tkinter import filedialog

#root window

def getMainWindow():
    root = tk.Tk()
    root.title("Calculator by Mateusz Dobija")
    root.geometry("400x490")
    root.resizable(width=False, height=False)
    root.resizable(width=False, height=False)
    root.rowconfigure(3, minsize=30)
    root.columnconfigure(3, minsize=30)
    return root
# Widgets are added here.

#functions
def button_click(clickedNumberOrSign):
    global display_str
    display_str = display_str + str(clickedNumberOrSign)
    display_string_var.set(display_str)

def button_result():
    global display_str
    try:
        result = str(eval(display_str))
        display_str = ""
        display_string_var.set(result)
    except:
        display_str = ""
        display_string_var.set("error")
def button_clear():
    global display_str
    display_str = ""
    display_string_var.set(display_str)

def button_delete():
    global display_str
    display_str = display_str[:-1]
    display_string_var.set(display_str)

def handle_eval_exception():
    global display_str
    display_str = display_str[:-1]
    display_string_var.set(display_str)

#display
def createDisplay():
    display_frame = tk.Frame(root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=4)
    #display = tk.Label(root, text="Hello", bg="grey", width=100) #, width=400, height=5
    #display.grid(row = 0, column = 0,sticky='news')
    display_frame.pack(side=tk.TOP)

    display = tk.Entry(display_frame, font=('arial', 18), textvariable=display_string_var, width=50, bg="grey", bd=0, justify=tk.RIGHT)
    display.pack()

#buttons
def createButtons():
    buttons_frame = tk.Frame(root, width=400, height=440, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=4, bg="grey")
    buttons_frame.pack()

    buttonClear = tk.Button(buttons_frame, text="C", bg="white", width=10, height=5, command=button_clear)
    buttonClear.grid(row=0, column=0, padx=1, pady=1)

    buttonDelete = tk.Button(buttons_frame, text="Del", bg="white", width=10, height=5, command=button_delete)
    buttonDelete.grid(row=0, column=1, padx=1, pady=1)

    buttonZero = tk.Button(buttons_frame, text="0", bg="white", width=10, height=5, command=lambda: button_click(0))
    buttonZero.grid(row=0, column=2, padx=1, pady=1)

    buttonMul = tk.Button(buttons_frame, text="*", bg="white", width=10, height=5, command=lambda: button_click("*"))
    buttonMul.grid(row=0, column=3, padx=1, pady=1)

    buttonSeven = tk.Button(buttons_frame, text="7", bg="white", width=10, height=5, command=lambda: button_click(7))
    buttonSeven.grid(row=1, column=0, padx=1, pady=1)

    buttonEight = tk.Button(buttons_frame, text="8", bg="white", width=10, height=5, command=lambda: button_click(8))
    buttonEight.grid(row=1, column=1)

    buttonNine = tk.Button(buttons_frame, text="9", bg="white", width=10, height=5, command=lambda: button_click(9))
    buttonNine.grid(row=1, column=2)

    buttonAdd = tk.Button(buttons_frame, text="+", bg="white", width=10, height=5, command=lambda: button_click("+"))
    buttonAdd.grid(row=1, column=3, padx=1, pady=1)

    buttonFour = tk.Button(buttons_frame, text="4", bg="white", width=10, height=5, command=lambda: button_click(4))
    buttonFour.grid(row=2, column=0)

    buttonFive = tk.Button(buttons_frame, text="5", bg="white", width=10, height=5, command=lambda: button_click(5))
    buttonFive.grid(row=2, column=1)

    buttonSix = tk.Button(buttons_frame, text="6", bg="white", width=10, height=5, command=lambda: button_click(6))
    buttonSix.grid(row=2, column=2)

    buttonSubtract = tk.Button(buttons_frame, text="-", bg="white", width=10, height=5, command=lambda: button_click("-"))
    buttonSubtract.grid(row=2, column=3, padx=1, pady=1)

    buttonOne = tk.Button(buttons_frame, text="1", bg="white", width=10, height=5, command=lambda: button_click(1))
    buttonOne.grid(row=3, column=0)

    buttonTwo = tk.Button(buttons_frame, text="2", bg="white", width=10, height=5, command=lambda: button_click(2))
    buttonTwo.grid(row=3, column=1)

    buttonThree = tk.Button(buttons_frame, text="3", bg="white", width=10, height=5, command=lambda: button_click(3))
    buttonThree.grid(row=3, column=2)

    buttonDivide = tk.Button(buttons_frame, text="/", bg="white", width=10, height=5, command=lambda: button_click("/"))
    buttonDivide.grid(row=3, column=3, padx=1, pady=1)

    buttonBrace1 = tk.Button(buttons_frame, text="(", bg="white", width=10, height=5, command=lambda: button_click("("))
    buttonBrace1.grid(row=4, column=0, padx=1, pady=1)

    buttonBrace2 = tk.Button(buttons_frame, text=")", bg="white", width=10, height=5, command=lambda: button_click(")"))
    buttonBrace2.grid(row=4, column=1, padx=1, pady=1)

    buttonComma = tk.Button(buttons_frame, text=",", bg="white", width=10, height=5, command=lambda: button_click("."))
    buttonComma.grid(row=4, column=2, padx=1, pady=1)

    buttonResult = tk.Button(buttons_frame, text="=", bg="white", width=10, height=5, command=button_result)
    buttonResult.grid(row=4, column=3, padx=1, pady=1)

def callback():
    print("called the callback!")

if __name__ == "__main__":
    root = getMainWindow()
    display_str = ""
    display_string_var = tk.StringVar()
    createDisplay()
    createButtons()
    root.mainloop()


#root przekazać jako argument
#stringVar - to samo
#pydoc - dokumentacja
#
#na 5: wersja obiektowa
