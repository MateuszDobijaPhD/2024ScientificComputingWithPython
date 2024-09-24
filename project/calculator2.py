"""
This is the documentation for the Calculator project.
The project has been presented as a final project for "Scientific Computing with Python" classes at the Jagiellonian University.

author: Mateusz Dobija
email: mateusz.dobija@doctoral.uj.edu.pl
academic year: 2023/2024
year of phd studies: III
program: Technical Computer Science and Telecommunication
classes: Scientific Computing with Python

To generate HTML documentation for this module issue the command:

    pydoc -w calculator2.py

"""
import tkinter as tk
from tkinter import filedialog

#root window
class Calculator:
    """
    Main class responsible for Calculator generation.
    Hold variables:
    - root -> Tk
        Responsible for main window
    - display_string_var
        StringVariable, which content is shown at the display of calculator
    - isLastClickedButtonResult
        Flag indicating if last clicked button was sign =.
    - isLastObtainedResultError
        Flag indicating if last obtained result was "error"
    """

    def __init__(self):
        #self.generateCalvulatot()
        pass
    def getMainWindow(self):
        """
        Function returning instance of main window. with set parameters like size, title, ability to resize.
        :return: root->Tk
            Instance of Tk class, representing main window of application
        """
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
    def isNumber(self, clickedNumberOrSign):
        """
        Function checking if element clickedNumberOrSign, passed as parameter, is number from 0 to 9.
        :param clickedNumberOrSign:
            Sign, e.g. +,-,/,*,(,) or a number from 0 to 9
        :return:
            True if clickedNumberOrSign contains a number,
            False if clickedNumberOrSign doesn't contain a number
        """
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if clickedNumberOrSign in numbers:
            return True
        return False
    def isBrace(self, clickedNumberOrSign):
        """
        Function checking if element clickedNumberOrSign, passed as parameter, is an opening or a closing brace.

        :param clickedNumberOrSign:
            Sign, e.g. +,-,/,*,(,) or a number from 0 to 9
        :return:
            True if clickedNumberOrSign contains a brace,
            False if clickedNumberOrSign doesn't contain a brace
        """
        if clickedNumberOrSign == "(" or clickedNumberOrSign == ")":
            return True
        return False

    def button_click(self, clickedNumberOrSign):
        """
        Function handling click on the button.
        If the last clicked button was =, and last obtain result was error, before further action clear the variable indicating string on a display.
        If the last clicked button was =, and currently handled button represents a number of a brace, before further action clear the variable indicating string on a display.

        :param clickedNumberOrSign:
            Sign, e.g. +,-,/,*,(,) or a number from 0 to 9
        :return:
        """
        if self.isLastClickedButtonResult.get() == True:
            if self.isLastObtainedResultError.get() == True:
                self.display_string_var.set("")
            elif (self.isNumber(clickedNumberOrSign) or self.isBrace(clickedNumberOrSign)):
                self.display_string_var.set("")

        self.display_string_var.set(self.display_string_var.get() + str(clickedNumberOrSign))
        self.isLastClickedButtonResult.set(False)

    def button_result(self):
        """
        Function handling click on "=" button.
        Calculates result from arithmetic operation typed at the calculator, and set result on a display string.
        If the evaluation error is raised, set "error" string on a display string.
        :return:
        """
        self.isLastClickedButtonResult.set(True)
        try:
            result = str(eval(self.display_string_var.get()))
            self.display_string_var.set(result)
            self.isLastObtainedResultError.set(False)
        except:
            self.display_string_var.set("error")
            self.isLastObtainedResultError.set(True)
    def button_clear(self):
        """
        Function handling click on "C" sign on calculator.
        Clear the display.
        :return:
        """
        display_str = ""
        self.display_string_var.set(display_str)
        self.isLastClickedButtonResult.set(False)

    def button_delete(self):
        """
        Function handling click on button "Del" on a calculator.
        Function delete last (from right side) element from display, so the last typed number or a sign.
        :return:
        """
        display_str = self.display_string_var.get()[:-1]
        self.display_string_var.set(display_str)
        self.isLastClickedButtonResult.set(False)

    #display
    def createDisplay(self):
        """
        Function responsible for creating a display of the calculator, and connecting instance's variable display_string_var as a string presented on a display.
        :return:
        """
        display_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=4)
        display_frame.pack(side=tk.TOP)

        display = tk.Entry(display_frame, font=('arial', 18), textvariable=self.display_string_var, width=50, bg="grey", bd=0, justify=tk.RIGHT)
        display.pack()

    #buttons
    def createButtons(self):
        """
        Function responsible for creating Frame containing buttons on a calculator.
        Connects particular button to proper functions handling click on them, passing number or sign to a handling function if needed.
        :return:
        """
        buttons_frame = tk.Frame(self.root, width=400, height=440, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=4, bg="grey")
        buttons_frame.pack()

        buttonClear = tk.Button(buttons_frame, text="C", bg="white", width=10, height=5, command=lambda: self.button_clear())
        buttonClear.grid(row=0, column=0, padx=1, pady=1)

        buttonDelete = tk.Button(buttons_frame, text="Del", bg="white", width=10, height=5, command=lambda: self.button_delete())
        buttonDelete.grid(row=0, column=1, padx=1, pady=1)

        buttonZero = tk.Button(buttons_frame, text="0", bg="white", width=10, height=5, command=lambda: self.button_click(0))
        buttonZero.grid(row=0, column=2, padx=1, pady=1)

        buttonMul = tk.Button(buttons_frame, text="*", bg="white", width=10, height=5, command=lambda: self.button_click("*"))
        buttonMul.grid(row=0, column=3, padx=1, pady=1)

        buttonSeven = tk.Button(buttons_frame, text="7", bg="white", width=10, height=5, command=lambda: self.button_click(7))
        buttonSeven.grid(row=1, column=0, padx=1, pady=1)

        buttonEight = tk.Button(buttons_frame, text="8", bg="white", width=10, height=5, command=lambda: self.button_click(8))
        buttonEight.grid(row=1, column=1)

        buttonNine = tk.Button(buttons_frame, text="9", bg="white", width=10, height=5, command=lambda: self.button_click(9))
        buttonNine.grid(row=1, column=2)

        buttonAdd = tk.Button(buttons_frame, text="+", bg="white", width=10, height=5, command=lambda: self.button_click("+"))
        buttonAdd.grid(row=1, column=3, padx=1, pady=1)

        buttonFour = tk.Button(buttons_frame, text="4", bg="white", width=10, height=5, command=lambda: self.button_click(4))
        buttonFour.grid(row=2, column=0)

        buttonFive = tk.Button(buttons_frame, text="5", bg="white", width=10, height=5, command=lambda: self.button_click(5))
        buttonFive.grid(row=2, column=1)

        buttonSix = tk.Button(buttons_frame, text="6", bg="white", width=10, height=5, command=lambda: self.button_click(6))
        buttonSix.grid(row=2, column=2)

        buttonSubtract = tk.Button(buttons_frame, text="-", bg="white", width=10, height=5, command=lambda: self.button_click("-"))
        buttonSubtract.grid(row=2, column=3, padx=1, pady=1)

        buttonOne = tk.Button(buttons_frame, text="1", bg="white", width=10, height=5, command=lambda: self.button_click(1))
        buttonOne.grid(row=3, column=0)

        buttonTwo = tk.Button(buttons_frame, text="2", bg="white", width=10, height=5, command=lambda: self.button_click(2))
        buttonTwo.grid(row=3, column=1)

        buttonThree = tk.Button(buttons_frame, text="3", bg="white", width=10, height=5, command=lambda: self.button_click(3))
        buttonThree.grid(row=3, column=2)

        buttonDivide = tk.Button(buttons_frame, text="/", bg="white", width=10, height=5, command=lambda: self.button_click("/"))
        buttonDivide.grid(row=3, column=3, padx=1, pady=1)

        buttonBrace1 = tk.Button(buttons_frame, text="(", bg="white", width=10, height=5, command=lambda: self.button_click("("))
        buttonBrace1.grid(row=4, column=0, padx=1, pady=1)

        buttonBrace2 = tk.Button(buttons_frame, text=")", bg="white", width=10, height=5, command=lambda: self.button_click(")"))
        buttonBrace2.grid(row=4, column=1, padx=1, pady=1)

        buttonComma = tk.Button(buttons_frame, text=",", bg="white", width=10, height=5, command=lambda: self.button_click("."))
        buttonComma.grid(row=4, column=2, padx=1, pady=1)

        buttonResult = tk.Button(buttons_frame, text="=", bg="white", width=10, height=5, command=lambda: self.button_result())
        buttonResult.grid(row=4, column=3, padx=1, pady=1)

    def callback(self):
        print("called the callback!")

    def generateCalculator(self):
        """
        Main function, generating a calculator and setting inctances' variables.
        :return:
        """
        self.root = self.getMainWindow()
        self.display_string_var = tk.StringVar()
        self.display_string_var.set("")
        self.isLastClickedButtonResult = tk.BooleanVar(value=False)
        self.isLastObtainedResultError = tk.BooleanVar(value=False)
        self.createDisplay()
        self.createButtons()
        self.root.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.generateCalculator()
