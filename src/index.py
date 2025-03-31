import tkinter as tk
from entities.sudoku_game import SudokuGame

def main():
    root = tk.Tk()
    app = SudokuGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
