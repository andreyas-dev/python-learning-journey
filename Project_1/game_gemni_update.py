import tkinter as tk
from tkinter import ttk
import random

class SnakeWaterGunApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # --- Window Configuration ---
        self.title("Snake Water Gun: Ultimate Edition 🎮")
        self.geometry("650x750")
        self.configure(bg="#1e1e1e") 
        self.resizable(False, False)

        # --- Game Variables ---
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.round_number = 1
        self.player_streak = 0
        self.computer_streak = 0
        self.tie_streak = 0
        self.max_player_streak = 0
        self.player_name = "Player"
        
        # NEW: Health and Timer Variables
        self.player_hp = 100
        self.computer_hp = 100
        self.time_left = 3
        self.timer_id = None

        self.user_dict = {'s': 1, 'w': -1, 'g': 0}
        self.reverse_dict = {1: 's', -1: 'w', 0: 'g'}
        self.words = {'s': 'Snake 🐍', 'w': 'Water 💧', 'g': 'Gun 🔫'}

        self.welcome_frame = tk.Frame(self, bg="#1e1e1e")
        self.game_frame = tk.Frame(self, bg="#1e1e1e")
        self.stats_frame = tk.Frame(self, bg="#1e1e1e")

        self.show_welcome_screen()

    # ==========================================
    # LOGIC FUNCTIONS (Your Exact Logic)
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
        tk.Label(self.welcome_frame, text="Snake Water Gun: Ultimate 🎮", bg="#1e1e1e", fg="#00FFFF", font=("Helvetica", 20, "bold")).pack()
        tk.Label(self.welcome_frame, text="="*40, bg="#1e1e1e", fg="#00FFFF", font=("Courier", 14)).pack()

        tk.Label(self.welcome_frame, text="Game Rules", bg="#1e1e1e", fg="#FF00FF", font=("Helvetica", 16, "bold")).pack(pady=(20, 5))
        rules = "1. Snake drinks Water.\n2. Water douses Gun.\n3. Gun kills Snake.\n\n⚠️ NEW: You have 3 seconds per turn!\nReduce the Computer's HP to 0 to win."
        tk.Label(self.welcome_frame, text=rules, bg="#1e1e1e", fg="white", font=("Helvetica", 14), justify="center").pack()

        tk.Label(self.welcome_frame, text="Enter your name:", bg="#1e1e1e", fg="white", font=("Helvetica", 14)).pack(pady=(30, 5))
        self.name_entry = tk.Entry(self.welcome_frame, font=("Helvetica", 14), justify="center")
        self.name_entry.pack(ipady=5)

        start_btn = tk.Button(self.welcome_frame, text="FIGHT!", font=("Helvetica", 16, "bold"), bg="#FFA500", fg="black", command=self.start_game)
        start_btn.pack(pady=30, ipadx=30, ipady=10)
        
        # Hover effect for start button
        start_btn.bind("<Enter>", lambda e: start_btn.config(bg="#FF4500", fg="white"))
        start_btn.bind("<Leave>", lambda e: start_btn.config(bg="#FFA500", fg="black"))

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

        for widget in self.game_frame.winfo_children():
            widget.destroy()

        # UI Setup
        self.round_label = tk.Label(self.game_frame, text=f"ROUND {self.round_number}", bg="#1e1e1e", fg="#5A9BD5", font=("Helvetica", 20, "bold"))
        self.round_label.pack(pady=(10, 10))

        # --- HEALTH BARS ---
        hp_frame = tk.Frame(self.game_frame, bg="#1e1e1e")
        hp_frame.pack(fill="x", padx=20, pady=10)

        # Player HP
        tk.Label(hp_frame, text=self.player_name, bg="#1e1e1e", fg="white", font=("Helvetica", 12, "bold")).grid(row=0, column=0, sticky="w")
        self.player_hp_bar = ttk.Progressbar(hp_frame, orient="horizontal", length=250, mode="determinate")
        self.player_hp_bar.grid(row=1, column=0, padx=(0, 20))
        self.player_hp_bar["value"] = self.player_hp

        # Computer HP
        tk.Label(hp_frame, text="Computer", bg="#1e1e1e", fg="white", font=("Helvetica", 12, "bold")).grid(row=0, column=1, sticky="e")
        self.comp_hp_bar = ttk.Progressbar(hp_frame, orient="horizontal", length=250, mode="determinate")
        self.comp_hp_bar.grid(row=1, column=1)
        self.comp_hp_bar["value"] = self.computer_hp

        # --- TIMER ---
        self.timer_label = tk.Label(self.game_frame, text="3", bg="#1e1e1e", fg="#FF4500", font=("Helvetica", 40, "bold"))
        self.timer_label.pack(pady=10)

        self.streak_label = tk.Label(self.game_frame, text="", bg="#1e1e1e", font=("Helvetica", 12, "bold"))
        self.streak_label.pack(pady=5)
        self.update_streak_display()

        self.status_label = tk.Label(self.game_frame, text="Make your choice!", bg="#1e1e1e", fg="white", font=("Helvetica", 16))
        self.status_label.pack(pady=20)

        # --- ACTION BUTTONS ---
        btn_frame = tk.Frame(self.game_frame, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        self.btn_snake = tk.Button(btn_frame, text="Snake 🐍", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", width=12, command=lambda: self.play_round('s'))
        self.btn_snake.grid(row=0, column=0, padx=10)
        self.btn_water = tk.Button(btn_frame, text="Water 💧", font=("Helvetica", 14, "bold"), bg="#2196F3", fg="white", width=12, command=lambda: self.play_round('w'))
        self.btn_water.grid(row=0, column=1, padx=10)
        self.btn_gun = tk.Button(btn_frame, text="Gun 🔫", font=("Helvetica", 14, "bold"), bg="#9E9E9E", fg="white", width=12, command=lambda: self.play_round('g'))
        self.btn_gun.grid(row=0, column=2, padx=10)

        # Hover Effects
        self.add_hover(self.btn_snake, "#4CAF50", "#66BB6A")
        self.add_hover(self.btn_water, "#2196F3", "#42A5F5")
        self.add_hover(self.btn_gun, "#9E9E9E", "#BDBDBD")

        self.start_timer()

    def add_hover(self, button, default_color, hover_color):
        button.bind("<Enter>", lambda e: button.config(bg=hover_color) if button['state'] == 'normal' else None)
        button.bind("<Leave>", lambda e: button.config(bg=default_color) if button['state'] == 'normal' else None)

    # --- TIMER LOGIC ---
    def start_timer(self):
        self.time_left = 3
        self.timer_label.config(text=str(self.time_left), fg="#FF4500")
        self.tick_timer()

    def tick_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=str(self.time_left))
            self.time_left -= 1
            self.timer_id = self.after(1000, self.tick_timer)
        else:
            self.timer_label.config(text="TIME's UP!", fg="red")
            self.play_round('timeout') # Force a loss if they don't click

    def play_round(self, user_choice):
        # Stop the timer!
        if self.timer_id:
            self.after_cancel(self.timer_id)

        # Disable buttons
        self.btn_snake.config(state="disabled")
        self.btn_water.config(state="disabled")
        self.btn_gun.config(state="disabled")

        if user_choice == 'timeout':
            self.status_label.config(text="Too slow! You lose 20 HP!", fg="red")
            self.after(1500, lambda: self.apply_damage('computer', None, None))
            return

        self.status_label.config(text="Computer is choosing...", fg="yellow")
        self.after(1000, lambda: self.resolve_round(user_choice))

    def resolve_round(self, user_choice):
        user_value = self.user_dict[user_choice]
        comp_value = self.get_computer_choice()
        winner = self.determine_winner(user_value, comp_value)

        comp_word = self.words[self.reverse_dict[comp_value]]
        user_word = self.words[user_choice]

        self.apply_damage(winner, user_word, comp_word)

    def apply_damage(self, winner, user_word, comp_word):
        if winner == 'tie':
            self.tie_score += 1
            self.tie_streak += 1
            self.player_streak = self.computer_streak = 0
            result_text = f"Computer chose: {comp_word}\nYou chose: {user_word}\n\nIt's a tie! 🤝\nNo damage dealt."
            color = "#FFD700" 
        elif winner == 'player':
            self.player_score += 1
            self.player_streak += 1
            if self.player_streak > self.max_player_streak:
                self.max_player_streak = self.player_streak
            self.computer_streak = self.tie_streak = 0
            self.computer_hp -= 20 # Deal damage
            result_text = f"Computer chose: {comp_word}\nYou chose: {user_word}\n\n{user_word} beats {comp_word}! 🎉\nComputer loses 20 HP!"
            color = "#00FF00" 
        else:
            self.computer_score += 1
            self.computer_streak += 1
            self.player_streak = self.tie_streak = 0
            self.player_hp -= 20 # Take damage
            
            if user_word: # Regular loss
                result_text = f"Computer chose: {comp_word}\nYou chose: {user_word}\n\n{comp_word} beats {user_word}! 😢\nYou lose 20 HP!"
            else: # Timeout loss
                result_text = "You took too long!\nYou lose 20 HP!"
            color = "#FF0000" 

        # Update HP Bars and text
        self.player_hp_bar["value"] = max(0, self.player_hp)
        self.comp_hp_bar["value"] = max(0, self.computer_hp)
        self.status_label.config(text=result_text, fg=color)
        self.round_number += 1
        
        # Check for game over
        if self.player_hp <= 0 or self.computer_hp <= 0:
            self.after(2000, self.show_stats_screen)
        else:
            self.after(2500, self.next_round_ui)

    def next_round_ui(self):
        self.round_label.config(text=f"ROUND {self.round_number}")
        self.update_streak_display()
        self.status_label.config(text="Make your choice!", fg="white")
        
        self.btn_snake.config(state="normal")
        self.btn_water.config(state="normal")
        self.btn_gun.config(state="normal")
        
        self.start_timer() # Restart timer for new round

    def update_streak_display(self):
        if self.player_streak > 1:
            self.streak_label.config(text=f"🔥 {self.player_name} is on a {self.player_streak}-win streak!", fg="#00FF00")
        elif self.computer_streak > 1:
            self.streak_label.config(text=f"💻 Computer is on a {self.computer_streak}-win streak!", fg="#FF0000")
        elif self.tie_streak > 1:
            self.streak_label.config(text=f"🤝 Tie streak of {self.tie_streak}!", fg="#FFD700")
        else:
            self.streak_label.config(text="") 

    # ==========================================
    # SCREEN 3: FINAL STATS SCREEN
    # ==========================================
    def show_stats_screen(self):
        self.game_frame.pack_forget()
        self.stats_frame.pack(expand=True, fill="both")

        total_round = self.player_score + self.computer_score + self.tie_score
        
        if total_round > 0:
            player_win_rate = (self.player_score / total_round)
            Computer_win_rate = (self.computer_score / total_round)
        else:
            player_win_rate = Computer_win_rate = 0

        tk.Label(self.stats_frame, text="=================== GAME OVER ===================", bg="#1e1e1e", fg="#00FFFF", font=("Courier", 12)).pack(pady=(20, 10))
        tk.Label(self.stats_frame, text=f"{self.player_name}: {self.player_score} | Computer: {self.computer_score} | Ties: {self.tie_score}", bg="#1e1e1e", fg="white", font=("Helvetica", 16, "bold")).pack()
        tk.Label(self.stats_frame, text="="*50, bg="#1e1e1e", fg="white").pack(pady=10)

        stats_text = (
            f"Total rounds played : {total_round}\n"
            f"{self.player_name}'s Win rate : {player_win_rate:.2%}\n"
            f"Computer's Win rate : {Computer_win_rate:.2%}\n"
            f"{self.player_name}'s longest winning streak is : {self.max_player_streak}"
        )
        tk.Label(self.stats_frame, text=stats_text, bg="#1e1e1e", fg="white", font=("Helvetica", 14), justify="left").pack(pady=10)

        # K.O. Logic based on Health
        if self.computer_hp <= 0:
            win_text = f"🏆 K.O.! You defeated the Computer! {self.player_name} Wins! 🎉"
            win_color = "#00FF00" 
        elif self.player_hp <= 0:
            win_text = "💀 K.O.! You were defeated by the Computer! Better luck next time. 😢"
            win_color = "#FF0000" 
        else:
            win_text = "🤝 Game Ended."
            win_color = "#FFD700" 

        tk.Label(self.stats_frame, text=win_text, bg="#1e1e1e", fg=win_color, font=("Helvetica", 18, "bold"), wraplength=500).pack(pady=30)

        quit_btn = tk.Button(self.stats_frame, text="Exit Game", font=("Helvetica", 14, "bold"), bg="#F44336", fg="white", command=self.destroy)
        quit_btn.pack(pady=20)
        
        self.add_hover(quit_btn, "#F44336", "#E53935")

if __name__ == "__main__":
    app = SnakeWaterGunApp()
    app.mainloop()