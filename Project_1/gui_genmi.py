
import tkinter as tk
from tkinter import messagebox
import random

class SnakeWaterGunApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # --- Window Configuration ---
        self.title("Snake Water Gun Game 🎮")
        self.geometry("600x650")
        self.configure(bg="#1e1e1e") # Dark theme background
        self.resizable(False, False)

        # --- Game Variables (Exact logic from your code) ---
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.round_number = 1
        self.player_streak = 0
        self.computer_streak = 0
        self.tie_streak = 0
        self.max_player_streak = 0
        self.player_name = "Player"

        # Mapping dictionaries
        self.user_dict = {'s': 1, 'w': -1, 'g': 0}
        self.reverse_dict = {1: 's', -1: 'w', 0: 'g'}
        self.words = {'s': 'Snake 🐍', 'w': 'Water 💧', 'g': 'Gun 🔫'}

        # --- Frames (Screens) ---
        self.welcome_frame = tk.Frame(self, bg="#1e1e1e")
        self.game_frame = tk.Frame(self, bg="#1e1e1e")
        self.stats_frame = tk.Frame(self, bg="#1e1e1e")

        # Start with the Welcome Screen
        self.show_welcome_screen()

    # ==========================================
    # LOGIC FUNCTIONS (Unchanged from your code)
    # ==========================================
    def get_computer_choice(self):
        return random.choice([1, -1, 0])

    def determine_winner(self, user_val, comp_val):
        if user_val == comp_val:
            return 'tie'
        elif comp_val - user_val == 1 or comp_val - user_val == -2:
            return 'computer'
        else:
            return 'player'

    # ==========================================
    # SCREEN 1: WELCOME SCREEN
    # ==========================================
    def show_welcome_screen(self):
        self.game_frame.pack_forget()
        self.stats_frame.pack_forget()
        self.welcome_frame.pack(expand=True, fill="both")

        tk.Label(self.welcome_frame, text="="*40, bg="#1e1e1e", fg="#00FFFF", font=("Courier", 14)).pack(pady=(20,0))
        tk.Label(self.welcome_frame, text="Welcome to Snake Water Gun Game 🎮", bg="#1e1e1e", fg="#00FFFF", font=("Helvetica", 18, "bold")).pack()
        tk.Label(self.welcome_frame, text="="*40, bg="#1e1e1e", fg="#00FFFF", font=("Courier", 14)).pack()

        tk.Label(self.welcome_frame, text="Game Rules", bg="#1e1e1e", fg="#FF00FF", font=("Helvetica", 16, "bold")).pack(pady=(20, 5))
        rules = "1.  Snake drinks Water.\n2.  Water douses Gun.\n3.  Gun kills Snake."
        tk.Label(self.welcome_frame, text=rules, bg="#1e1e1e", fg="white", font=("Helvetica", 14), justify="left").pack()

        tk.Label(self.welcome_frame, text="Enter your name:", bg="#1e1e1e", fg="white", font=("Helvetica", 14)).pack(pady=(30, 5))
        self.name_entry = tk.Entry(self.welcome_frame, font=("Helvetica", 14), justify="center")
        self.name_entry.pack(ipady=5)

        start_btn = tk.Button(self.welcome_frame, text="Press to Start", font=("Helvetica", 14, "bold"), bg="#FFA500", fg="black", command=self.start_game)
        start_btn.pack(pady=30, ipadx=20, ipady=10)

    def start_game(self):
        name = self.name_entry.get().strip().capitalize()
        if name:
            self.player_name = name
        self.show_game_screen()

    # ==========================================
    # SCREEN 2: MAIN GAME SCREEN
    # ==========================================
    def show_game_screen(self):
        self.welcome_frame.pack_forget()
        self.game_frame.pack(expand=True, fill="both")

        # Clear old widgets
        for widget in self.game_frame.winfo_children():
            widget.destroy()

        # Round Label (Blue)
        self.round_label = tk.Label(self.game_frame, text=f"========== ROUND {self.round_number} ==========", bg="#1e1e1e", fg="#5A9BD5", font=("Helvetica", 16, "bold"))
        self.round_label.pack(pady=(20, 10))

        # Score Label
        score_text = f"Scores -> {self.player_name}: {self.player_score} | Computer: {self.computer_score} | Ties: {self.tie_score}"
        self.score_label = tk.Label(self.game_frame, text=score_text, bg="#1e1e1e", fg="white", font=("Helvetica", 14))
        self.score_label.pack()

        # Streak Label
        self.streak_label = tk.Label(self.game_frame, text="", bg="#1e1e1e", font=("Helvetica", 12, "bold"))
        self.streak_label.pack(pady=5)
        self.update_streak_display()

        # Status/Suspense Label
        self.status_label = tk.Label(self.game_frame, text="Make your choice!", bg="#1e1e1e", fg="white", font=("Helvetica", 16))
        self.status_label.pack(pady=30)

        # Buttons Frame
        btn_frame = tk.Frame(self.game_frame, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        self.btn_snake = tk.Button(btn_frame, text="Snake 🐍", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", width=10, command=lambda: self.play_round('s'))
        self.btn_snake.grid(row=0, column=0, padx=10)

        self.btn_water = tk.Button(btn_frame, text="Water 💧", font=("Helvetica", 14, "bold"), bg="#2196F3", fg="white", width=10, command=lambda: self.play_round('w'))
        self.btn_water.grid(row=0, column=1, padx=10)

        self.btn_gun = tk.Button(btn_frame, text="Gun 🔫", font=("Helvetica", 14, "bold"), bg="#9E9E9E", fg="white", width=10, command=lambda: self.play_round('g'))
        self.btn_gun.grid(row=0, column=2, padx=10)

        # End Game Button
        end_btn = tk.Button(self.game_frame, text="End Game & Show Final Scores", font=("Helvetica", 12), bg="#F44336", fg="white", command=self.show_stats_screen)
        end_btn.pack(side="bottom", pady=30)

    def play_round(self, user_choice):
        # Disable buttons to prevent spam clicking
        self.btn_snake.config(state="disabled")
        self.btn_water.config(state="disabled")
        self.btn_gun.config(state="disabled")

        # Simulate countdown/suspense
        self.status_label.config(text="Computer is choosing...", fg="yellow")
        
        # Wait 1.5 seconds, then calculate result
        self.after(1500, lambda: self.resolve_round(user_choice))

    def resolve_round(self, user_choice):
        user_value = self.user_dict[user_choice]
        comp_value = self.get_computer_choice()
        winner = self.determine_winner(user_value, comp_value)

        comp_word = self.words[self.reverse_dict[comp_value]]
        user_word = self.words[user_choice]

        # Determine winner and apply exact logic
        if winner == 'tie':
            self.tie_score += 1
            self.tie_streak += 1
            self.player_streak = self.computer_streak = 0
            result_text = f"Computer chose: {comp_word}\nYou chose: {user_word}\n\nIt's a tie! 🤝"
            color = "#FFD700" # Yellow
        elif winner == 'player':
            self.player_score += 1
            self.player_streak += 1
            if self.player_streak > self.max_player_streak:
                self.max_player_streak = self.player_streak
            self.computer_streak = self.tie_streak = 0
            result_text = f"Computer chose: {comp_word}\nYou chose: {user_word}\n\n{user_word} beats {comp_word}! You Win! 🎉"
            color = "#00FF00" # Green
        else:
            self.computer_score += 1
            self.computer_streak += 1
            self.player_streak = self.tie_streak = 0
            result_text = f"Computer chose: {comp_word}\nYou chose: {user_word}\n\n{comp_word} beats {user_word}! You lose! 😢"
            color = "#FF0000" # Red

        # Update Labels
        self.status_label.config(text=result_text, fg=color)
        self.round_number += 1
        
        # Prepare next round UI after 2.5 seconds
        self.after(2500, self.next_round_ui)

    def next_round_ui(self):
        self.round_label.config(text=f"========== ROUND {self.round_number} ==========")
        score_text = f"Scores -> {self.player_name}: {self.player_score} | Computer: {self.computer_score} | Ties: {self.tie_score}"
        self.score_label.config(text=score_text)
        self.update_streak_display()
        
        self.status_label.config(text="Make your choice!", fg="white")
        
        # Re-enable buttons
        self.btn_snake.config(state="normal")
        self.btn_water.config(state="normal")
        self.btn_gun.config(state="normal")

    def update_streak_display(self):
        if self.player_streak > 1:
            self.streak_label.config(text=f"🔥 {self.player_name} is on a {self.player_streak}-win streak!", fg="#00FF00")
        elif self.computer_streak > 1:
            self.streak_label.config(text=f"💻 Computer is on a {self.computer_streak}-win streak!", fg="#FF0000")
        elif self.tie_streak > 1:
            self.streak_label.config(text=f"🤝 Tie streak of {self.tie_streak}!", fg="#FFD700")
        else:
            self.streak_label.config(text="") # Clear streak label

    # ==========================================
    # SCREEN 3: FINAL STATS SCREEN
    # ==========================================
    def show_stats_screen(self):
        self.game_frame.pack_forget()
        self.stats_frame.pack(expand=True, fill="both")

        # Total Calculation (Exact logic)
        total_round = self.player_score + self.computer_score + self.tie_score
        if total_round == 0:
            tk.Label(self.stats_frame, text="No rounds played!", bg="#1e1e1e", fg="white", font=("Helvetica", 16)).pack(pady=50)
            return

        player_win_rate = (self.player_score / total_round)
        Computer_win_rate = (self.computer_score / total_round)

        tk.Label(self.stats_frame, text="=================== FINAL SCORES ===================", bg="#1e1e1e", fg="#00FFFF", font=("Courier", 12)).pack(pady=(20, 10))
        tk.Label(self.stats_frame, text=f"{self.player_name}: {self.player_score} | Computer: {self.computer_score} | Ties: {self.tie_score}", bg="#1e1e1e", fg="white", font=("Helvetica", 16, "bold")).pack()
        tk.Label(self.stats_frame, text="="*50, bg="#1e1e1e", fg="white").pack(pady=10)

        tk.Label(self.stats_frame, text=f"========== {self.player_name}'s Game Statistics ==========", bg="#1e1e1e", fg="#00FFFF", font=("Courier", 12)).pack(pady=(10, 10))
        
        stats_text = (
            f"Total rounds played : {total_round}\n"
            f"{self.player_name}'s Win rate : {player_win_rate:.2%}\n"
            f"Computer's Win rate : {Computer_win_rate:.2%}\n"
            f"{self.player_name}'s longest winning streak is : {self.max_player_streak}"
        )
        tk.Label(self.stats_frame, text=stats_text, bg="#1e1e1e", fg="white", font=("Helvetica", 14), justify="left").pack()

        # Overall Winner logic
        if self.player_score > self.computer_score:
            win_text = f"🏆 Congratulations! You are the overall winner! {self.player_name} 🎉"
            win_color = "#00FF00" # Green
        elif self.computer_score > self.player_score:
            win_text = "💻 Computer wins overall! Better luck next time! 😢"
            win_color = "#FF0000" # Red
        else:
            win_text = "🤝 It's an overall tie! Great game!"
            win_color = "#FFD700" # Yellow

        tk.Label(self.stats_frame, text=win_text, bg="#1e1e1e", fg=win_color, font=("Helvetica", 16, "bold"), wraplength=500).pack(pady=30)

        # Quit Button
        quit_btn = tk.Button(self.stats_frame, text="Exit Game", font=("Helvetica", 14, "bold"), bg="#F44336", fg="white", command=self.destroy)
        quit_btn.pack(pady=20)

if __name__ == "__main__":
    app = SnakeWaterGunApp()
    app.mainloop()