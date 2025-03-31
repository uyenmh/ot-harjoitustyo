import tkinter as tk
from tkinter import ttk, messagebox
from sudoku import Sudoku

class SudokuGame:
    def __init__(self, root):
        self.initial_root = root
        self.game_root = None
        self.initial_root.title("Sudoku")
        self.difficulty = tk.StringVar(value="Easy")
        self.puzzle = None
        self.solution = None
        self.game_board = []
        self.choose_difficulty()

    def choose_difficulty(self):
        mainframe = ttk.Frame(self.initial_root, padding=10)
        mainframe.pack()

        ttk.Label(mainframe, text="Choose difficulty level:").pack()

        difficulty = ttk.Combobox(mainframe, textvariable=self.difficulty, state="readonly")
        difficulty["values"] = ("Easy", "Medium", "Hard")
        difficulty.current()
        difficulty.pack()

        ttk.Button(mainframe, text="Start game", command=self.start_game).pack(padx=120, pady=(10,5))
        ttk.Button(mainframe, text="Exit game", command=self.exit_game).pack(padx=120, pady=(10,5))

    def start_game(self):
        difficulty = self.difficulty.get()
        if difficulty == "Easy":
            difficulty = 0.3
        elif difficulty == "Medium":
            difficulty = 0.45
        else:
            difficulty = 0.6

        self.initial_root.destroy()

        self.game_root = tk.Tk()
        self.game_root.title("Sudoku")
        self.puzzle = Sudoku(3).difficulty(difficulty)
        self.solution = self.puzzle.solve()
        self.create_sudoku()

    def exit_game(self):
        self.initial_root.destroy()

    def create_sudoku(self):
        mainframe = ttk.Frame(self.game_root, padding=30)
        mainframe.pack()
        
        # AI generated code starts here 
        for row in range(9):
            row_cells = []
            for col in range(9):
                preset_value = self.puzzle.board[row][col]
                entry = ttk.Entry(mainframe, width=3, font=('Arial', 20), justify='center')
                entry.grid(row=row, column=col, padx=2, pady=2)
                if preset_value:
                    entry.insert(0, str(preset_value))
                    entry.config(state='disabled')
                row_cells.append(entry)
            self.game_board.append(row_cells)
        
        ttk.Button(self.game_root, text="Check Solution", command=self.check_solution).pack(pady=(0,5))
        # AI generated code ends here

        ttk.Button(self.game_root, text="End game", command=self.end_game).pack(pady=(10,20))

    def end_game(self):
        self.game_root.destroy()

    # AI generated code starts here 
    def check_solution(self):
        for row in range(9):
            for col in range(9):
                if self.game_board[row][col].get() != str(self.solution.board[row][col]):
                    messagebox.showerror("Error", "Incorrect solution!")
                    return
        messagebox.showinfo("Success", "Congratulations! You solved the Sudoku!")
    # AI generated code ends here
