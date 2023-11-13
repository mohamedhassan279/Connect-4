import tkinter as tk
from tkinter import messagebox
import random

import MiniMax
from Heuristic.Heuristic import Heuristic
from Heuristic.Heuristic1 import Heuristic1
from Heuristic.Heuristic2 import Heuristic2
from MiniMax.MinimaxWithPruning import MinimaxWithPruning
from MiniMax.MinimaxWoPruning import MinimaxWoPruning
from State import State


class GUI:
    def __init__(self, master):

        self.state = State()
        self.heuristic = None
        self.minimax = None

        self.master = master
        self.master.title("Connect 4 Game")
        # Initialize game variables
        self.board = [['' for _ in range(7)] for _ in range(6)]
        self.current_player = None
        self.turn = False
        self.human_color = ''
        self.computer_color = ''
        self.human_score = 0
        self.computer_score = 0
        self.max_depth = 4
        self.initial_depth = 4
        self.use_pruning = tk.BooleanVar(value=True)  # Default to use pruning
        self.heuristic_choice = tk.IntVar(value=1)  # Default heuristic 1
        self.game_running = False

        # GUI elements
        self.top_frame = tk.Frame(master, bg=bg_color_hex)
        self.top_frame.pack(side=tk.TOP)




        self.sidebar_frame = tk.Frame(master, width=400, bg="#{:02x}{:02x}{:02x}".format(*(95, 95, 95)))
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.game_frame = tk.Frame(master)
        self.game_frame.pack(side=tk.LEFT, padx=50, pady=0)  # Added padx and pady to create space around the game grid

        # Top elements
        self.human_score_label = tk.Label(self.top_frame, text="Human Score: 0", font=("Arial", 12), bg=bg_color_hex, fg='white')
        #self.human_score_label.grid(row=0, column=0, padx=10, pady=5)
        self.human_score_label.pack(side=tk.LEFT, padx=10)

        self.computer_score_label = tk.Label(self.top_frame, text="Computer Score: 0", font=("Arial", 12), bg=bg_color_hex, fg='white')
        # self.computer_score_label.grid(row=0, column=1, padx=10, pady=5)
        self.computer_score_label.pack(side=tk.RIGHT, padx=10)

        # Sidebar elements
        self.choose_color_label = tk.Label(self.sidebar_frame, text="Choose Your Color:")
        self.choose_color_label.pack(pady=10)

        self.color_var = tk.StringVar(value='Red')  # Default color for human player
        self.color_var.trace_add('write', self.update_color)
        self.color_radio_red = tk.Radiobutton(self.sidebar_frame, text='Red', variable=self.color_var, value='Red')
        self.color_radio_yellow = tk.Radiobutton(self.sidebar_frame, text='Yellow', variable=self.color_var,
                                                 value='Yellow')
        self.color_radio_red.pack()
        self.color_radio_yellow.pack()

        # StringVar for max_depth_entry
        self.max_depth_var = tk.StringVar(value=str(self.max_depth))
        self.max_depth_var.trace_add('write', self.update_max_depth)

        # Max Depth Entry
        self.max_depth_label = tk.Label(self.sidebar_frame, text="Choose Max Depth:")
        self.max_depth_label.pack(pady=10)

        self.max_depth_entry = tk.Entry(self.sidebar_frame, validate="key",
                                        validatecommand=(self.sidebar_frame.register(self.validate_entry), '%P'),
                                        textvariable=self.max_depth_var)  # Use the StringVar here
        self.max_depth_entry.pack()

        # Use Pruning Radiobutton
        self.pruning_label = tk.Label(self.sidebar_frame, text="Use Pruning:")
        self.pruning_label.pack(pady=10)

        self.pruning_radio_on = tk.Radiobutton(self.sidebar_frame, text='Yes', variable=self.use_pruning, value=True)
        self.pruning_radio_off = tk.Radiobutton(self.sidebar_frame, text='No', variable=self.use_pruning, value=False)
        self.pruning_radio_on.pack()
        self.pruning_radio_off.pack()

        # Heuristic Choice Radiobutton
        self.heuristic_label = tk.Label(self.sidebar_frame, text="Choose Heuristic:")
        self.heuristic_label.pack(pady=10)

        self.heuristic_radio_1 = tk.Radiobutton(self.sidebar_frame, text='Heuristic 1', variable=self.heuristic_choice,
                                                value=1)
        self.heuristic_radio_2 = tk.Radiobutton(self.sidebar_frame, text='Heuristic 2', variable=self.heuristic_choice,
                                                value=2)
        self.heuristic_radio_1.pack()
        self.heuristic_radio_2.pack()

        # self.use_pruning.trace_add('write', self.update_pruning)
        # self.heuristic_choice.trace_add('write', self.update_heuristic)


        # Game Canvas
        self.canvas = tk.Canvas(self.game_frame, width=500, height=500, bg='blue')
        self.canvas.pack()  # Center the canvas in the game frame

        # Initialize game
        self.initialize_game()

    def validate_entry(self, value):
        # Validate function to allow only integer values
        return value.isdigit() or value == ''

    def update_color(self, *args):
        self.human_color = self.color_var.get()
        self.computer_color = 'Yellow' if self.human_color == 'Red' else 'Red'

    def update_max_depth(self, *args):
        # Function to update max_depth when max_depth_var changes
        max_depth_value = self.max_depth_var.get()
        self.max_depth = int(max_depth_value) if max_depth_value.isdigit() else 4
        print("Max Depth:", self.max_depth)

    # def update_pruning(self, *args):
    #     self.use_pruning.get()
    #
    # def update_heuristic(self, *args):
    #     self.heuristic_choice.get()

    def initialize_game(self):
        # Initialize game based on user choices (color, max depth, pruning, heuristic)
        self.max_depth = int(self.max_depth_entry.get()) if self.max_depth_entry.get().isdigit() else 4

        # Draw initial board
        self.draw_board()

        # Set up initial player
        self.current_player = self.human_color

        # Update color selection with colored indicators
        self.update_selection()

        # Print default values for testing
        print("Max Depth:", self.max_depth_var.get())
        print("Use Pruning:", self.use_pruning.get())
        print("Heuristic Choice:", self.heuristic_choice.get())

    # def start_game(self):
    #     if self.game_running:
    #         # If the game is already running, reset the game
    #         self.reset_game()
    #     else:
    #         # Print default values for testing
    #         print("st Max Depth:", self.max_depth_var)
    #         print("st Use Pruning:", self.use_pruning)
    #         print("st Heuristic Choice:", self.heuristic_choice)
    #         self.init_game()
    #         # If the game is not running, start the game
    #         self.human_color = self.color_var.get()
    #         self.computer_color = 'Yellow' if self.human_color == 'Red' else 'Red'
    #         self.current_player = self.human_color  # Set to human player first
    #
    #         # Start the game loop
    #         self.canvas.bind("<Button-1>", self.on_column_click)
    #         self.start_button.config(text="Restart Game")  # Change button text to indicate restart
    #         self.game_running = True  # Set the flag to indicate that the game is running

    def init_game(self):
        print("init game " , self.heuristic_choice.get(), " ", self.use_pruning.get())
        self.heuristic = self.take_heuristic(self.heuristic_choice.get())
        self.minimax = self.take_minimax(self.heuristic, self.use_pruning.get())

    def reset_game(self):
        self.init_game()
        self.initial_depth = self.max_depth
        self.board = [['' for _ in range(7)] for _ in range(6)]
        self.human_score = 0
        self.computer_score = 0
        self.turn = False

        self.current_player = self.human_color
        self.draw_board()
        self.start_button.config(text="Start Game")  # Change button text back to "Start Game"
        self.game_running = False  # Set the flag to indicate that the game is not running

    def update_selection(self):
        # Destroy existing color selection widgets
        for widget in self.sidebar_frame.winfo_children():
            if isinstance(widget, (tk.Radiobutton, tk.Label, tk.Entry)):
                widget.destroy()

        # Choose Color label
        self.choose_color_label = tk.Label(self.sidebar_frame, text="Choose Your Color:")
        self.choose_color_label.pack(pady=10)

        # Color selection radiobuttons with colored indicators
        colors = [('Red', 'red'), ('Yellow', 'yellow')]
        for color, color_code in colors:
            radio_button = tk.Radiobutton(self.sidebar_frame, text=color, variable=self.color_var, value=color,
                                          indicatoron=False, width=10)
            radio_button.config(bg=color_code, activebackground=color_code, selectcolor=color_code)
            radio_button.pack()

        # Max Depth Entry
        # StringVar for max_depth_entry
        self.max_depth_var = tk.StringVar(value=str(self.max_depth))
        self.max_depth_var.trace_add('write', self.update_max_depth)

        # Max Depth Entry
        self.max_depth_label = tk.Label(self.sidebar_frame, text="Choose Max Depth:")
        self.max_depth_label.pack(pady=10)

        self.max_depth_entry = tk.Entry(self.sidebar_frame, validate="key",
                                        validatecommand=(self.sidebar_frame.register(self.validate_entry), '%P'),
                                        textvariable=self.max_depth_var)  # Use the StringVar here
        self.max_depth_entry.pack()

        # Use Pruning Radiobutton
        self.pruning_label = tk.Label(self.sidebar_frame, text="Use Pruning:")
        self.pruning_label.pack(pady=10)

        self.pruning_radio_on = tk.Radiobutton(self.sidebar_frame, text='Yes', variable=self.use_pruning,
                                               value=True)
        self.pruning_radio_off = tk.Radiobutton(self.sidebar_frame, text='No', variable=self.use_pruning,
                                                value=False)
        self.pruning_radio_on.pack()
        self.pruning_radio_off.pack()

        # Heuristic Choice Radiobutton
        self.heuristic_label = tk.Label(self.sidebar_frame, text="Choose Heuristic:")
        self.heuristic_label.pack(pady=10)

        self.heuristic_radio_1 = tk.Radiobutton(self.sidebar_frame, text='Heuristic 1',
                                                variable=self.heuristic_choice,
                                                value=1)
        self.heuristic_radio_2 = tk.Radiobutton(self.sidebar_frame, text='Heuristic 2',
                                                variable=self.heuristic_choice,
                                                value=2)
        self.heuristic_radio_1.pack()
        self.heuristic_radio_2.pack()

        # self.use_pruning.trace_add('write', self.update_pruning)
        # self.heuristic_choice.trace_add('write', self.update_heuristic)

        # Other sidebar elements (scores)
        self.start_button = tk.Button(self.sidebar_frame, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)



    def start_game(self):
        # Print default values for testing
        print("Max Depth:", self.max_depth)
        print("Use Pruning:", self.use_pruning.get())
        print("Heuristic Choice:", self.heuristic_choice.get())

        if self.game_running:
            # If the game is already running, reset the game
            self.reset_game()
        else:
            self.init_game()
            self.initial_depth = self.max_depth
            # If the game is not running, start the game
            self.human_color = self.color_var.get()
            self.computer_color = 'Yellow' if self.human_color == 'Red' else 'Red'
            self.current_player = self.human_color  # Set to human player first

            # Start the game loop
            self.canvas.bind("<Button-1>", self.on_column_click)
            self.start_button.config(text="Restart Game")  # Change button text to indicate restart
            self.game_running = True  # Set the flag to indicate that the game is running

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(6):
            for col in range(7):
                x1, y1 = col * 70 + 10, row * 70 + 30
                x2, y2 = x1 + 60, y1 + 60
                # Set empty circle color to white
                fill_color = 'white' if self.board[row][col] == '' else self.board[row][col]
                self.canvas.create_oval(x1, y1, x2, y2, fill=fill_color, outline='black')


    def take_minimax(self, heuristic: Heuristic, use_pruning_attr):
        if use_pruning_attr:
            return MinimaxWithPruning(heuristic)
        return MinimaxWoPruning(heuristic)

    def take_heuristic(self, heuristic_int):
        if heuristic_int == 1:
            print("init game heuristic", heuristic_int)
            return Heuristic1()
        return Heuristic2()




    def on_column_click(self, event):
        col = event.x // 70
        print("selected col ")
        print(col)
        if self.is_valid_move(col):
            self.make_move(col)
            #update state according to human move
            self.state.drop_chip(col)

            self.draw_board()

            if self.check_winner():
                self.display_winner(self.current_player)
            else:
                self.current_player = self.computer_color
                #call the computer agent
                grid = self.state.convert_to_board()
                computer_col, h_best_state, minimax_pointer = self.minimax.get_best_move(self.state, self.initial_depth)
                actual_col = self.get_actual_col(grid, computer_col + 1)
                self.state.drop_chip(actual_col)
                print("heuristic col ", computer_col)
                print("computer col ", actual_col)
                self.make_move(actual_col)
                # self.computer_move()
                self.draw_board()
                print(self.state.convert_to_board())
                if self.check_winner():
                    self.display_winner(self.current_player)
                else:
                    self.current_player = self.human_color

        else:
            print("not valid")

    def get_actual_col(self, grid, computer_col):
        for j in range(7):

            if grid[5][j] == 0:
                computer_col -= 1
                if computer_col == 0:
                    return j


    def is_valid_move(self, col):
        return self.board[0][col] == ''

    def make_move(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == '':
                self.board[row][col] = self.current_player
                break

    def check_winner(self):
        # Implement your winning condition check here
        pass

    def display_winner(self, winner):
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_game()

    # def reset_game(self):
    #     self.board = [['' for _ in range(7)] for _ in range(6)]
    #     self.current_player = self.human_color
    #     self.draw_board()
    #     self.start_button.config(state=tk.NORMAL)

    def computer_move(self):
        # Implement a basic AI move (minimax)
        col = self.minimax(self.board, self.max_depth, True)[0]
        if self.is_valid_move(col):
            self.make_move(col)

    def minimax(self, board, depth, maximizing_player):
        # Basic minimax implementation for AI move
        # You can enhance this with alpha-beta pruning for better performance
        if depth == 0 or self.check_winner():
            return None, self.evaluate_board()

        valid_moves = [col for col in range(7) if self.is_valid_move(col)]

        if maximizing_player:
            value = float('-inf')
            best_col = random.choice(valid_moves)
            for col in valid_moves:
                temp_board = [row[:] for row in board]
                self.make_move(col)
                _, temp_value = self.minimax(temp_board, depth - 1, False)
                if temp_value > value:
                    value = temp_value
                    best_col = col
                self.undo_move(col)
            return best_col, value
        else:
            value = float('inf')
            best_col = random.choice(valid_moves)
            for col in valid_moves:
                temp_board = [row[:] for row in board]
                self.make_move(col)
                _, temp_value = self.minimax(temp_board, depth - 1, True)
                if temp_value < value:
                    value = temp_value
                    best_col = col
                self.undo_move(col)
            return best_col, value

    def evaluate_board(self):
        # Basic evaluation function for AI move
        # You can enhance this based on your heuristic
        return 0

    def undo_move(self, col):
        for row in range(6):
            if self.board[row][col] != '':
                self.board[row][col] = ''
                break

# Create the main application window
root = tk.Tk()
root.geometry("800x600")

bg_color_rgb = (51, 50, 48)
bg_color_hex = "#{:02x}{:02x}{:02x}".format(*bg_color_rgb)

root.configure(bg=bg_color_hex)

# Create and run the GUI instance
game = GUI(root)

# Start the Tkinter event loop
root.mainloop()




