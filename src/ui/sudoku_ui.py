import tkinter as tk
from tkinter import ttk, messagebox
from entities.sudoku_game import SudokuGame


class SudokuUI:
    def __init__(self, root):
        self.initial_root = root
        self.game_root = None
        self.initial_root.title("Sudoku")
        self.difficulty = tk.StringVar(value="Easy")
        self.puzzle = None
        self.game_board = []
        self.game = None
        self.timer_running = False
        
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

    def exit_game(self):
        if self.game_root:
            self.game_root.destroy()
        self.initial_root.destroy()

    def start_game(self):
        self.game = SudokuGame(self.difficulty.get())

        self.initial_root.destroy()

        self.game_root = tk.Tk()
        self.game_root.title("Sudoku")
        self.create_sudoku()

    def create_sudoku(self):
        self.timer = tk.Label(
            self.game_root,
            text="00:00:00",
            font=('Arial', 15),
            fg="gray",
            relief="ridge",
            bd=2,
            padx=10,
            pady=5
        )
        self.timer.pack(pady=(30, 0))
    
        mainframe = ttk.Frame(self.game_root, padding=30)
        mainframe.pack()

        self.timer_running = True
        self.update_timer()

        self.puzzle = self.game.get_puzzle_board()
        
        # AI generated code starts here 
        for row in range(9):
            row_cells = []
            for col in range(9):
                preset_value = self.puzzle[row][col]
                entry = ttk.Entry(mainframe, width=3, font=('Arial', 20), justify='center')
                entry.grid(row=row, column=col, padx=2, pady=2)
                if preset_value:
                    entry.insert(0, str(preset_value))
                    entry.config(state='disabled')
                row_cells.append(entry)
            self.game_board.append(row_cells)
        
        ttk.Button(self.game_root, text="Check Solution", command=self.check_solution).pack(pady=(0,5))
        # AI generated code ends here

        ttk.Button(self.game_root, text="End game", command=self.end_game).pack(pady=(10,5))
        ttk.Button(self.game_root, text="Exit game", command=self.exit_game).pack(pady=(10,20))

    def update_timer(self):
        if not self.timer_running:
            return 
        hours, minutes, seconds = self.game.get_elapsed_time()
        self.timer.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.game_root.after(1000, self.update_timer) 

    def end_game(self):
        self.game_root.destroy()
        new_root = tk.Tk()
        SudokuUI(new_root)

    def check_solution(self):
        if self.game.is_solution_correct(self.game_board):
            self.timer_running = False 
            hours, minutes, seconds = self.game.get_elapsed_time()
            if hours > 0 and minutes > 0:
                messagebox.showinfo("Success", f"Congratulations! You solved the Sudoku!\nTime: {hours}h {minutes}m {seconds}s")
            elif hours == 0 and minutes > 0:
                messagebox.showinfo("Success", f"Congratulations! You solved the Sudoku!\nTime: {minutes}m {seconds}s")
            else:
                messagebox.showinfo("Success", f"Congratulations! You solved the Sudoku!\nTime: {seconds}s")
        else:
            messagebox.showerror("Error", "Incorrect solution!")
