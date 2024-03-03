"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user to enter their name.
    goofyahhname = simpledialog.askstring(None, prompt="GIVE ME YOU NAME BOZO!!!!!!!")
    potato = ""
    q = 2
    for c in goofyahhname:
        if q % 2 == 0:
            beans = c.upper()
            potato = potato + beans
        else:
            beans2 = c.lower()
            potato = potato + beans2
        q = q + 1

    messagebox.showinfo(None, message=potato)

    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    pass