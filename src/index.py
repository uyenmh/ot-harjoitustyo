import tkinter as tk
from ui.sudoku_ui import SudokuUI


def main():
    root = tk.Tk()
    app = SudokuUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
