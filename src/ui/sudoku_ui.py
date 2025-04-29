import tkinter as tk
from tkinter import ttk, messagebox
from services.sudoku_game import SudokuService


class SudokuUI:
    """A class responsible for the user interface."""

    def __init__(self, root):
        """The class constructor. Initializes the main menu for the game.

        Args:
            root (tk.Tk): A Tkinter element used to initialize the UI.
        """

        self.initial_root = root
        self.game_root = None
        self.leaderboard_root = None
        self.initial_root.title("Sudoku")
        self.difficulty = tk.StringVar(value="Easy")
        self.game_board = []
        self.game = None
        self.timer_running = False
        self.timer_id = None
        self.elapsed_time = 0
        self.name_entry = None
        self.check_solution_button = None
        self.save_score_button = None
        self.pause_game_button = None
        self.continue_game_button = None

        self.choose_difficulty()

    def choose_difficulty(self):
        """Displays the difficulty selection screen."""

        mainframe = ttk.Frame(
            self.initial_root,
            padding=10
        )
        mainframe.pack()

        ttk.Label(
            mainframe,
            text="Choose difficulty level:",
            font=("Calibri", 10)
        ).pack(pady=(0,2))

        difficulty = ttk.Combobox(
            mainframe,
            textvariable=self.difficulty,
            state="readonly",
            font=("Calibri", 10)
        )
        difficulty["values"] = ("Easy", "Medium", "Hard")
        difficulty.pack()

        self.initial_root.option_add("*TCombobox*Listbox.font", ("Calibri", 10))

        button_style = ttk.Style()
        button_style.configure("my.TButton", font=("Calibri", 10))

        ttk.Button(
            mainframe,
            text="Start game",
            style="my.TButton",
            command=self.start_game
        ).pack(padx=120, pady=(15,5))

        ttk.Button(
            mainframe,
            text="View leaderboard",
            style="my.TButton",
            command=self.view_leaderboard
        ).pack(pady=(10,5))

        ttk.Button(
            mainframe,
            text="Exit game",
            style="my.TButton",
            command=self.exit_game
        ).pack(padx=120, pady=(10,5))

    def start_game(self):
        """Initializes a new game based on the difficulty chosen."""

        self.game = SudokuService(self.difficulty.get())

        self.initial_root.destroy()

        self.game_root = tk.Tk()
        self.game_root.title("Sudoku")
        self.create_sudoku()

    def create_sudoku(self):
        """Displays the Sudoku game, its timer and other controls."""

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

        mainframe = ttk.Frame(
            self.game_root,
            padding=30)
        mainframe.pack()

        self.timer_running = True
        self.update_timer()

        puzzle = self.game.get_puzzle_board()
        vcmd = (self.game_root.register(self.validate_game_entries), '%P')

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
                block_frame.grid(
                    row=block_row,
                    column=block_col,
                    padx=2,
                    pady=2
                )

                for i in range(3):
                    for j in range(3):
                        row = block_row * 3 + i
                        col = block_col * 3 + j
                        preset_value = puzzle[row][col]

                        entry = tk.Entry(
                            block_frame,
                            width=3,
                            font=("lucidatypewriter", 20),
                            justify="center",
                            relief="solid",
                            bd=1,
                            validate="key",
                            validatecommand=vcmd
                        )

                        entry.grid(
                            row=i,
                            column=j,
                            padx=1,
                            pady=1
                        )

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

        pause_buttons_frame = ttk.Frame(self.game_root)
        pause_buttons_frame.pack(pady=(0, 5))

        self.pause_game_button = ttk.Button(
            pause_buttons_frame,
            text="Pause game",
            style="my.TButton",
            command=self.pause_game
        )
        self.pause_game_button.pack(
            side="left",
            padx=(0, 5)
        )

        self.continue_game_button = ttk.Button(
            pause_buttons_frame,
            text="Continue game",
            style="my.TButton",
            command=self.continue_game
        )
        self.continue_game_button.pack(
            side="left",
            padx=(5, 0)
        )
        self.continue_game_button["state"] = "disabled"

        self.check_solution_button = ttk.Button(
            self.game_root,
            text="Check Solution",
            style="my.TButton",
            command=self.check_solution
        )
        self.check_solution_button.pack(pady=(10,5))

        name_entry_frame = ttk.Frame(self.game_root)
        name_entry_frame.pack(pady=(10, 0))

        ttk.Label(
            name_entry_frame,
            text="Enter name:",
            font=("Calibri", 10)
        ).pack(pady=(0,1))
        self.name_entry = ttk.Entry(
            name_entry_frame,
            width=13
        )
        self.name_entry.pack()

        self.save_score_button = ttk.Button(
            self.game_root,
            text="Save score",
            style="my.TButton",
            command=self.save_game_score
        )
        self.save_score_button.pack(pady=(10,5))
        self.save_score_button["state"] = "disabled"

        leave_game_buttons_frame = ttk.Frame(self.game_root)
        leave_game_buttons_frame.pack(pady=(10, 20))

        ttk.Button(
            leave_game_buttons_frame,
            text="View leaderboard",
            style="my.TButton",
            command=self.view_leaderboard
        ).pack(side="left", padx=(0, 5))

        ttk.Button(
            leave_game_buttons_frame,
            text="Return to menu",
            style="my.TButton",
            command=self.return_to_menu
        ).pack(side="left", padx=(5, 5))

        ttk.Button(
            leave_game_buttons_frame,
            text="Exit game",
            style="my.TButton",
            command=self.exit_game
        ).pack(side="left", padx=(5, 0))

    def validate_game_entries(self, input):
        """Validates the entries for the Sudoku game.

        Args:
            input (str): The current input for the Sudoku board cell.

        Returns:
            bool: True if input is a single digit between 1-9, False otherwise.
        """

        if len(input) == 1 and input in "123456789":
            return True
        elif len(input) == 0:
            return True
        else:
            return False

    def update_timer(self):
        """Updates the game timer every second if the timer is running."""

        if not self.timer_running:
            return
        hours, minutes, seconds, _ = self.game.get_elapsed_time_for_current_game()
        self.timer.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.timer_id = self.game_root.after(1000, self.update_timer)

    def pause_game(self):
        """Pauses the game and its timer."""

        self.timer_running = False
        self.game.pause_game()

        self.pause_game_button["state"] = "disabled"
        self.continue_game_button["state"] = "normal"

    def continue_game(self):
        """Continues the game and resumes its timer."""

        self.timer_running = True
        self.game.continue_game()
        self.update_timer()

        self.continue_game_button["state"] = "disabled"
        self.pause_game_button["state"] = "normal"

    def save_game_score(self):
        """Saves the score to the database if the solution is correct."""

        if self.game.is_solution_correct:
            if self.name_entry.get():
                self.game.save_score(self.name_entry.get(), self.difficulty.get(), self.elapsed_time)
            else:
                self.game.save_score("unknown", self.difficulty.get(), self.elapsed_time)
        self.save_score_button["state"] = "disabled"

    def view_leaderboard(self):
        """Displays the leaderboard, sorted by difficulty level."""

        current_root = None
        view_leaderboard = None

        if self.game_root:
            current_root = self.game_root
            if self.check_solution_button.instate(["disabled"]):
                view_leaderboard = True
            else:
                view_leaderboard = messagebox.askyesno(
                    title="View leaderboard",
                    message="Are you sure you want to view the leaderboard? " \
                    "All of the current game progress will be lost."
                )
            self.game_root.after_cancel(self.timer_id)
            self.timer_running = False
        else:
            current_root = self.initial_root
            view_leaderboard = True

        if not view_leaderboard:
            return

        current_root.destroy()

        self.leaderboard_root = tk.Tk()
        self.leaderboard_root.title("Sudoku Leaderboard")

        scores = SudokuService().show_leaderboard()

        leaderboard_frame = ttk.Frame(
            self.leaderboard_root,
            padding=40)
        leaderboard_frame.pack(padx=50)

        ttk.Label(
            leaderboard_frame,
            text="Leaderboard",
            font=("Calibri", 20)
        ).pack(pady=(0, 20))

        ttk.Label(
            leaderboard_frame,
            text="Hard",
            font=("Calibri", 15)
        ).pack(pady=(0, 20))
        for score in scores[0]:
            ttk.Label(
                leaderboard_frame,
                text=score,
                font=("Calibri", 15)
            ).pack(anchor="w")

        ttk.Label(
            leaderboard_frame,
            text="Medium",
            font=("Calibri", 15)
        ).pack(pady=(20, 20))
        for score in scores[1]:
            ttk.Label(
                leaderboard_frame,
                text=score,
                font=("Calibri", 15)
            ).pack(anchor="w")

        ttk.Label(
            leaderboard_frame,
            text="Easy",
            font=("Calibri", 15)
        ).pack(pady=(20, 20))
        for score in scores[2]:
            ttk.Label(
                leaderboard_frame,
                text=score,
                font=("Calibri", 15)
            ).pack(anchor="w")

        button_style = ttk.Style()
        button_style.configure("my.TButton", font=("Calibri", 10))

        ttk.Button(
            self.leaderboard_root,
            text="Return to menu",
            style="my.TButton",
            command=self.return_to_menu
        ).pack(pady=(0,10))
        ttk.Button(
            self.leaderboard_root,
            text="Exit game",
            style="my.TButton",
            command=self.exit_game
        ).pack(pady=(0,20))

    def exit_game(self):
        """Closes the application if the user confirms."""

        current_root = None
        exit_game = None

        if self.leaderboard_root:
            current_root = self.leaderboard_root
        elif self.game_root:
            current_root = self.game_root
        else:
            current_root = self.initial_root

        if current_root == self.game_root:
            exit_game = messagebox.askyesno(
                title="Exit game",
                message="Are you sure you want to exit the game? " \
                "All of the current game progress will be lost and the application will be closed."
            )
        else:
            exit_game = messagebox.askyesno(
                title="Exit game",
                message="Are you sure you want to exit the game? This will close the application."
            )

        if not exit_game:
            return
        
        current_root.destroy()

    def return_to_menu(self):
        """Returns to the main menu."""

        current_root = None
        return_to_menu = None

        if self.leaderboard_root:
            current_root = self.leaderboard_root
            return_to_menu = True
        elif self.game_root:
            current_root = self.game_root
            if self.check_solution_button.instate(["disabled"]):
                return_to_menu = True
            else:
                return_to_menu = messagebox.askyesno(
                    title="Return to menu",
                    message="Are you sure you want to return to menu? " \
                    "All of the current game progress will be lost."
                )
            self.game_root.after_cancel(self.timer_id)
            self.timer_running = False

        if not return_to_menu:
            return 
        
        current_root.destroy()
        new_root = tk.Tk()
        SudokuUI(new_root)

    def check_solution(self):
        """Checks the user's solution and displays a success or error message."""

        if self.game.is_solution_correct(self.game_board):
            self.timer_running = False
            hours, minutes, seconds, self.elapsed_time = self.game.get_elapsed_time_for_current_game()
            self.save_score_button["state"] = "normal"
            if hours > 0:
                messagebox.showinfo(
                    "Success",
                    f"Congratulations! You solved the Sudoku!\nTime: {hours}h {minutes}m {seconds}s"
                )
            elif hours == 0 and minutes > 0:
                messagebox.showinfo(
                    "Success",
                    f"Congratulations! You solved the Sudoku!\nTime: {minutes}m {seconds}s"
                )
            else:
                messagebox.showinfo(
                    "Success",
                    f"Congratulations! You solved the Sudoku!\nTime: {seconds}s"
                )

            self.check_solution_button["state"] = "disabled"
        else:
            messagebox.showerror(
                "Error",
                "Incorrect solution."
            )
