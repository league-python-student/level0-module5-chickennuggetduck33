"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user for a number
    number = simpledialog.askinteger(title=None, prompt="give me a number")
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    a = 0
    b = 2
    for i in range(number):
        if number % b == 0:
            a = a+1
            b = b+1
        else:
            b = b+1
    if a > 1:
        messagebox.showinfo(None, message=str(number)+" is not prime")
    else:
        messagebox.showinfo(None, message=str(number)+" is prime")

    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
