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
def isNumber(clickedNumberOrSign):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if clickedNumberOrSign in numbers:
        return True
    return False
def isBrace(clickedNumberOrSign):
    if clickedNumberOrSign == "(" or clickedNumberOrSign == ")":
        return True
    return False

def button_click(clickedNumberOrSign, display_string_var, isLastClickedButtonResult, isLastObtainedResultError):
    if isLastClickedButtonResult.get() == True:
        if isLastObtainedResultError.get() == True:
            display_string_var.set("")
        elif (isNumber(clickedNumberOrSign) or isBrace(clickedNumberOrSign)):
            display_string_var.set("")

    display_string_var.set(display_string_var.get() + str(clickedNumberOrSign))
    isLastClickedButtonResult.set(False)

def button_result(display_string_var, isLastClickedButtonResult, isLastObtainedResultError):
    isLastClickedButtonResult.set(True)
    try:
        result = str(eval(display_string_var.get()))
        display_string_var.set(result)
        isLastObtainedResultError.set(False)
    except:
        display_string_var.set("error")
        isLastObtainedResultError.set(True)
def button_clear(display_string_var, isLastClickedButtonResult):
    display_str = ""
    display_string_var.set(display_str)
    isLastClickedButtonResult.set(False)

def button_delete(display_string_var, isLastClickedButtonResult):
    display_str = display_string_var.get()[:-1]
    display_string_var.set(display_str)
    isLastClickedButtonResult.set(False)

#display
def createDisplay(root, display_string_var):
    display_frame = tk.Frame(root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=4)
    display_frame.pack(side=tk.TOP)

    display = tk.Entry(display_frame, font=('arial', 18), textvariable=display_string_var, width=50, bg="grey", bd=0, justify=tk.RIGHT)
    display.pack()

#buttons
def createButtons(root, display_string_var, isLastClickedButtonResult, isLastObtainedResultError):
    buttons_frame = tk.Frame(root, width=400, height=440, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=4, bg="grey")
    buttons_frame.pack()

    buttonClear = tk.Button(buttons_frame, text="C", bg="white", width=10, height=5, command=lambda: button_clear( display_string_var, isLastClickedButtonResult))
    buttonClear.grid(row=0, column=0, padx=1, pady=1)

    buttonDelete = tk.Button(buttons_frame, text="Del", bg="white", width=10, height=5, command=lambda: button_delete(display_string_var, isLastClickedButtonResult))
    buttonDelete.grid(row=0, column=1, padx=1, pady=1)

    buttonZero = tk.Button(buttons_frame, text="0", bg="white", width=10, height=5, command=lambda: button_click(0, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonZero.grid(row=0, column=2, padx=1, pady=1)

    buttonMul = tk.Button(buttons_frame, text="*", bg="white", width=10, height=5, command=lambda: button_click("*", display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonMul.grid(row=0, column=3, padx=1, pady=1)

    buttonSeven = tk.Button(buttons_frame, text="7", bg="white", width=10, height=5, command=lambda: button_click(7, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonSeven.grid(row=1, column=0, padx=1, pady=1)

    buttonEight = tk.Button(buttons_frame, text="8", bg="white", width=10, height=5, command=lambda: button_click(8, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonEight.grid(row=1, column=1)

    buttonNine = tk.Button(buttons_frame, text="9", bg="white", width=10, height=5, command=lambda: button_click(9, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonNine.grid(row=1, column=2)

    buttonAdd = tk.Button(buttons_frame, text="+", bg="white", width=10, height=5, command=lambda: button_click("+", display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonAdd.grid(row=1, column=3, padx=1, pady=1)

    buttonFour = tk.Button(buttons_frame, text="4", bg="white", width=10, height=5, command=lambda: button_click(4, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonFour.grid(row=2, column=0)

    buttonFive = tk.Button(buttons_frame, text="5", bg="white", width=10, height=5, command=lambda: button_click(5, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonFive.grid(row=2, column=1)

    buttonSix = tk.Button(buttons_frame, text="6", bg="white", width=10, height=5, command=lambda: button_click(6, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonSix.grid(row=2, column=2)

    buttonSubtract = tk.Button(buttons_frame, text="-", bg="white", width=10, height=5, command=lambda: button_click("-", display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonSubtract.grid(row=2, column=3, padx=1, pady=1)

    buttonOne = tk.Button(buttons_frame, text="1", bg="white", width=10, height=5, command=lambda: button_click(1, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonOne.grid(row=3, column=0)

    buttonTwo = tk.Button(buttons_frame, text="2", bg="white", width=10, height=5, command=lambda: button_click(2, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonTwo.grid(row=3, column=1)

    buttonThree = tk.Button(buttons_frame, text="3", bg="white", width=10, height=5, command=lambda: button_click(3, display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonThree.grid(row=3, column=2)

    buttonDivide = tk.Button(buttons_frame, text="/", bg="white", width=10, height=5, command=lambda: button_click("/", display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonDivide.grid(row=3, column=3, padx=1, pady=1)

    buttonBrace1 = tk.Button(buttons_frame, text="(", bg="white", width=10, height=5, command=lambda: button_click("(", display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonBrace1.grid(row=4, column=0, padx=1, pady=1)

    buttonBrace2 = tk.Button(buttons_frame, text=")", bg="white", width=10, height=5, command=lambda: button_click(")", display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonBrace2.grid(row=4, column=1, padx=1, pady=1)

    buttonComma = tk.Button(buttons_frame, text=",", bg="white", width=10, height=5, command=lambda: button_click(".", display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonComma.grid(row=4, column=2, padx=1, pady=1)

    buttonResult = tk.Button(buttons_frame, text="=", bg="white", width=10, height=5, command=lambda: button_result(display_string_var, isLastClickedButtonResult, isLastObtainedResultError))
    buttonResult.grid(row=4, column=3, padx=1, pady=1)

def callback():
    print("called the callback!")

def generateCalvulatot():
    root = getMainWindow()
    display_string_var = tk.StringVar()
    display_string_var.set("")
    isLastClickedButtonResult = tk.BooleanVar(value=False)
    isLastObtainedResultError = tk.BooleanVar(value=False)
    createDisplay(root, display_string_var)
    createButtons(root, display_string_var, isLastClickedButtonResult, isLastObtainedResultError)
    root.mainloop()

if __name__ == "__main__":

    generateCalvulatot()

#pydoc - dokumentacja
#
#na 5: wersja obiektowa
