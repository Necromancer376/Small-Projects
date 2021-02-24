from tkinter import *
import Sudoku_Solver

sudoku = [
			[5, 3, 0,  0, 7, 0,  0, 0, 0],
			[6, 0 ,0,  1, 9, 5,  0, 0, 0],
			[0, 9, 8,  0, 0, 0,  0, 6, 0],

			[8, 0, 0,  0, 6, 0,  0, 0, 3],
			[4, 0, 0,  8, 0, 3,  0, 0, 1],
			[7, 0, 0,  0, 2, 0,  0, 0, 6],

			[0, 6, 0,  0, 0, 0,  2, 8, 0],
			[0, 0, 0,  4, 1, 9,  0, 0, 5],
			[0, 0, 0,  0, 8, 0,  0, 7, 9]
		]

solved = [
            [5, 3, 0,  0, 7, 0,  0, 0, 0],
            [6, 0 ,0,  1, 9, 5,  0, 0, 0],
            [0, 9, 8,  0, 0, 0,  0, 6, 0],

            [8, 0, 0,  0, 6, 0,  0, 0, 3],
            [4, 0, 0,  8, 0, 3,  0, 0, 1],
            [7, 0, 0,  0, 2, 0,  0, 0, 6],

            [0, 6, 0,  0, 0, 0,  2, 8, 0],
            [0, 0, 0,  4, 1, 9,  0, 0, 5],
            [0, 0, 0,  0, 8, 0,  0, 7, 9]
        ]
Sudoku_Solver.Solve(solved)


def CallSolve():
    Sudoku_Solver.Solve(sudoku)
    for i in range(1, 10):
        for j in range(1, 10):
            
            cube = Entry(window, width=2)
            cube.insert(END, sudoku[i-1][j-1])

            cube.grid(row=i, column=j)


def PrintGrid():
    for i in range(9):
        for j in range(9):
            temp = sudoku[i][j]
            box = Entry(window, width=2)

            if temp !=0:
                box.insert(END, temp)

            box.grid(row=i+1, column=j+1)


def Help():
    pass


window = Tk()
window.geometry("600x400")
window.title("Sudoku")

PrintGrid()
solve_button = Button(window, text="Solve", command=CallSolve)
solve_button.grid(row=0, column=0)
help_button = Button(window, text="Help", command=Help)
help_button.grid(row=0, column=2)

window.mainloop()
