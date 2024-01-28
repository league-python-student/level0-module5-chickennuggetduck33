"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    Window = Tk()
    Window.withdraw()
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    pettype = simpledialog.askstring(None, prompt="do you want a dog a cat a kangaroo or an axolotl")
    petpoints = 0
    while True:
        dothing = simpledialog.askstring(None, prompt="walk, feed, or play")
        messagebox.showinfo(None, message="you "+dothing+" your "+pettype)
        petpoints = petpoints + 1
        if petpoints == 10:
            break
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
