# Using tkinter as the GUI - cannot run in VM Vagrant
import tkinter


def game():
    window = tkinter.Tk()
    window.title('Sudoku Game')
    # Will call an endless loop of the window until the user interaction closes it
    window.mainloop()


if __name__ == '__main__':
    game()
