import tkinter as tk
from tkinter import ttk, messagebox
from services.sudoku_game import SudokuGame


class SudokuUI:
    def __init__(self, root):
        self.initial_root = root
        self.game_root = None
        self.leaderboard_root = None
        self.initial_root.title("Sudoku")
        self.difficulty = tk.StringVar(value="Easy")
        self.puzzle = None
        self.game_board = []
        self.game = None
        self.timer_running = False
        self.elapsed_time = 0
        self.name_entry = None
        self.check_solution_button = None
        self.save_score_button = None

        self.choose_difficulty()

    def choose_difficulty(self):
        mainframe = ttk.Frame(self.initial_root, padding=10)
        mainframe.pack()

        ttk.Label(mainframe, text="Choose difficulty level:", font=("Calibri", 10)).pack(pady=(0,2))

        difficulty = ttk.Combobox(mainframe, textvariable=self.difficulty, state="readonly", font=("Calibri", 10))
        difficulty["values"] = ("Easy", "Medium", "Hard")
        difficulty.pack()

        self.initial_root.option_add("*TCombobox*Listbox.font", ("Calibri", 10))

        button_style = ttk.Style()
        button_style.configure("my.TButton", font=("Calibri", 10))

        ttk.Button(mainframe, text="Start game", style="my.TButton", command=self.start_game).pack(padx=120, pady=(15,5))
        ttk.Button(mainframe, text="View leaderboard", style="my.TButton", command=self.view_leaderboard).pack(pady=(10,5))
        ttk.Button(mainframe, text="Exit game", style="my.TButton", command=self.exit_game).pack(padx=120, pady=(10,5))

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
            font=("Calibri", 15),
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
        for block_row in range(3):
            row_cells = []
            for block_col in range(3):
                block_frame = tk.Frame(
                    mainframe,
                    highlightbackground="black",
                    highlightcolor="black",
                    highlightthickness=2
                )
                block_frame.grid(row=block_row, column=block_col, padx=2, pady=2)

                for i in range(3):
                    for j in range(3):
                        row = block_row * 3 + i
                        col = block_col * 3 + j
                        preset_value = self.puzzle[row][col]

                        entry = tk.Entry(
                            block_frame,
                            width=3,
                            font=("lucidatypewriter", 20),
                            justify="center",
                            relief="solid",
                            bd=1
                        )

                        entry.grid(row=i, column=j, padx=1, pady=1)

                        if preset_value:
                            entry.insert(0, str(preset_value))
                            entry.config(state="disabled")

                        if len(self.game_board) <= row:
                            self.game_board.append([])
                        self.game_board[row].append(entry)

            self.game_board.append(row_cells)
        # AI generated code ends here

        button_style = ttk.Style()
        button_style.configure("my.TButton", font=("Calibri", 10))

        self.check_solution_button = ttk.Button(self.game_root, text="Check Solution", style="my.TButton", command=self.check_solution)
        self.check_solution_button.pack(pady=(0,5))

        name_entry_frame = ttk.Frame(self.game_root)
        name_entry_frame.pack(pady=(10, 0))

        ttk.Label(name_entry_frame, text="Enter name:", font=("Calibri", 10)).pack(pady=(0,1))
        self.name_entry = ttk.Entry(name_entry_frame, width=13)
        self.name_entry.pack()

        self.save_score_button = ttk.Button(self.game_root, text="Save score", style="my.TButton", command=self.save_game_score)
        self.save_score_button.pack(pady=(10,5))
        self.save_score_button["state"] = "disabled"

        ttk.Button(self.game_root, text="View leaderboard", style="my.TButton", command=self.view_leaderboard).pack(pady=(10,5))
        ttk.Button(self.game_root, text="Return to menu", style="my.TButton", command=self.return_to_menu).pack(pady=(10,5))
        ttk.Button(self.game_root, text="Exit game", style="my.TButton", command=self.exit_game).pack(pady=(10,20))

    def update_timer(self):
        if not self.timer_running:
            return
        hours, minutes, seconds, _ = self.game.get_elapsed_time()
        self.timer.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.game_root.after(1000, self.update_timer)

    def save_game_score(self):
        if self.game.is_solution_correct:
            if self.name_entry.get():
                self.game.save_score(self.name_entry.get(), self.difficulty.get(), self.elapsed_time)
            else:
                self.game.save_score("unknown", self.difficulty.get(), self.elapsed_time)
        self.save_score_button["state"] = "disabled"

    def view_leaderboard(self):
        if self.game_root:
            self.game_root.destroy()
        else:
            self.initial_root.destroy()

        self.leaderboard_root = tk.Tk()
        self.leaderboard_root.title("Sudoku Leaderboard")

        scores = SudokuGame().show_leaderboard()

        leaderboard_frame = ttk.Frame(self.leaderboard_root, padding=40)
        leaderboard_frame.pack(padx=50)

        ttk.Label(leaderboard_frame, text="Leaderboard", font=("Calibri", 20)).pack(pady=(0, 20))

        ttk.Label(leaderboard_frame, text="Hard", font=("Calibri", 15)).pack(pady=(0, 20))
        for score in scores[0]:
            ttk.Label(leaderboard_frame, text=score, font=("Calibri", 15)).pack(anchor="w")

        ttk.Label(leaderboard_frame, text="Medium", font=("Calibri", 15)).pack(pady=(20, 20))
        for score in scores[1]:
            ttk.Label(leaderboard_frame, text=score, font=("Calibri", 15)).pack(anchor="w")

        ttk.Label(leaderboard_frame, text="Easy", font=("Calibri", 15)).pack(pady=(20, 20))
        for score in scores[2]:
            ttk.Label(leaderboard_frame, text=score, font=("Calibri", 15)).pack(anchor="w")

        button_style = ttk.Style()
        button_style.configure("my.TButton", font=("Calibri", 10))

        ttk.Button(self.leaderboard_root, text="Return to menu", style="my.TButton", command=self.return_to_menu).pack(pady=(0,10))
        ttk.Button(self.leaderboard_root, text="Exit game", style="my.TButton", command=self.exit_game).pack(pady=(0,20))

    def exit_game(self):
        if self.leaderboard_root:
            self.leaderboard_root.destroy()
        elif self.game_root:
            self.game_root.destroy()
        else:
            self.initial_root.destroy()

    def return_to_menu(self):
        if self.leaderboard_root:
            self.leaderboard_root.destroy()
        elif self.game_root.destroy():
            self.game_root.destroy()
        new_root = tk.Tk()
        SudokuUI(new_root)

    def check_solution(self):
        if self.game.is_solution_correct(self.game_board):
            self.timer_running = False
            hours, minutes, seconds, self.elapsed_time = self.game.get_elapsed_time()
            self.save_score_button["state"] = "normal"
            if hours > 0:
                messagebox.showinfo("Success", f"Congratulations! You solved the Sudoku!\nTime: {hours}h {minutes}m {seconds}s")
            elif hours == 0 and minutes > 0:
                messagebox.showinfo("Success", f"Congratulations! You solved the Sudoku!\nTime: {minutes}m {seconds}s")
            else:
                messagebox.showinfo("Success", f"Congratulations! You solved the Sudoku!\nTime: {seconds}s")

            self.check_solution_button["state"] = "disabled"
        else:
            messagebox.showerror("Error", "Incorrect solution!")
