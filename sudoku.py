# Using tkinter as the GUI - cannot run in VM Vagrant
import tkinter

sudoku_values = [[0] * 9] * 9
entries = []


def game():
    start()


def start():
    window = tkinter.Tk()
    window.title('Sudoku Game')
    menu = tkinter.Menu(window)
    menu.add_command(label='New', command='hi')
    window.config(menu=menu)
    # Will call an endless loop of the window until the user interaction closes it
    generateGrid(window)
    tkinter.Button(window, text="Save", command=updateSudoku).grid(
        row=9, column=0, sticky="nsew")
    window.mainloop()


def generateGrid(window):
    frame = tkinter.Frame(window, borderwidth=5,
                          relief="sunken", width=300, height=310)
    frame.grid(column=0, row=0, columnspan=9, rowspan=9)
    for idx_i, i in enumerate(sudoku_values):
        row = []
        for idx_j, j in enumerate(i):
            label_grid = tkinter.Entry(frame, text='', width=1)
            label_grid.grid(row=idx_i, column=idx_j)
            label_grid.insert(0, '0')
            row.append(label_grid)
        entries.append(row)


def updateSudoku():
    for idx_i, i in enumerate(entries):
        for idx_j, j in enumerate(i):
            print('hi  ', j.get())
    # sudoku_values[idx_i][idx_j] = j.get()


if __name__ == '__main__':
    game()
