# =========================================================
# 🎮 Snake Water Gun Game (GUI Version)
# ---------------------------------------------------------
# A fun and interactive terminal-based Snake Water Gun game
# built with Python and Tkinter GUI. Features clickable buttons,
# colored output, score tracking, win streaks, and statistics.
#
# 👤 Author: Andreyas
# 🐍 Language: Python (3.14)
# 💻 Platform: Terminal / GUI
# 🔢 Version: v2.0 (GUI)
# =========================================================

import random
import tkinter as tk
from tkinter import messagebox

# =========================
# Game Logic (unchanged)
# =========================

# Mapping dictionaries
user_dict = {'s': 1, 'w': -1, 'g': 0}
reverse_dict = {1: 's', -1: 'w', 0: 'g'}
words = {'s': 'Snake 🐍', 'w': 'Water 💧', 'g': 'Gun 🔫'}

# Scores and streaks
player_score = 0
computer_score = 0
tie_score = 0
player_streak = 0
computer_streak = 0
tie_streak = 0
max_player_streak = 0
round_number = 1
player_name = ""

def get_computer_choice():
    return random.choice([1, -1, 0])

def determine_winner(user_val, comp_val):
    if user_val == comp_val:
        return 'tie'
    elif comp_val - user_val == 1 or comp_val - user_val == -2:
        return 'computer'
    else:
        return 'player'

# =========================
# Tkinter GUI Setup
# =========================

root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("600x550")
root.resizable(False, False)

# =========================
# UI Variables
# =========================
player_name_var = tk.StringVar()
player_score_var = tk.StringVar(value="Player: 0")
computer_score_var = tk.StringVar(value="Computer: 0")
tie_score_var = tk.StringVar(value="Ties: 0")
round_var = tk.StringVar(value="Round: 1")
streak_var = tk.StringVar(value="")

# =========================
# UI Components
# =========================

tk.Label(root, text="🎮 Snake Water Gun Game", font=("Arial", 20, "bold")).pack(pady=10)

tk.Label(root, text="Enter your name:", font=("Arial", 12)).pack(pady=5)
player_entry = tk.Entry(root, textvariable=player_name_var, font=("Arial", 12))
player_entry.pack(pady=5)

# Scores
score_frame = tk.Frame(root)
score_frame.pack(pady=10)
tk.Label(score_frame, textvariable=player_score_var, font=("Arial", 14)).grid(row=0, column=0, padx=10)
tk.Label(score_frame, textvariable=computer_score_var, font=("Arial", 14)).grid(row=0, column=1, padx=10)
tk.Label(score_frame, textvariable=tie_score_var, font=("Arial", 14)).grid(row=0, column=2, padx=10)

tk.Label(root, textvariable=round_var, font=("Arial", 14, "bold")).pack(pady=5)
tk.Label(root, textvariable=streak_var, font=("Arial", 12, "italic"), fg="orange").pack(pady=5)

# Result display
result_text = tk.Text(root, height=5, width=60, font=("Arial", 12))
result_text.pack(pady=10)
result_text.config(state="disabled")

# =========================
# Game Logic Integration
# =========================

def update_result_text(message):
    result_text.config(state="normal")
    result_text.insert(tk.END, message + "\n")
    result_text.see(tk.END)
    result_text.config(state="disabled")

def play_round(choice):
    global player_score, computer_score, tie_score
    global player_streak, computer_streak, tie_streak, max_player_streak
    global round_number, player_name

    if not player_name_var.get().strip():
        messagebox.showwarning("Input Error", "Please enter your name first!")
        return
    player_name = player_name_var.get().strip().capitalize()

    user_val = user_dict[choice]
    comp_val = get_computer_choice()
    winner = determine_winner(user_val, comp_val)

    # Determine winner & update scores
    if winner == "tie":
        tie_score += 1
        tie_streak += 1
        player_streak = computer_streak = 0
        update_result_text(f"Round {round_number}: It's a tie! 🤝")
    elif winner == "player":
        player_score += 1
        player_streak += 1
        if player_streak > max_player_streak:
            max_player_streak = player_streak
        computer_streak = tie_streak = 0
        update_result_text(f"Round {round_number}: {words[choice]} beats {words[reverse_dict[comp_val]]}! You Win! 🎉")
    else:
        computer_score += 1
        computer_streak += 1
        player_streak = tie_streak = 0
        update_result_text(f"Round {round_number}: {words[reverse_dict[comp_val]]} beats {words[choice]}! You lose! 😢")

    # Update UI
    player_score_var.set(f"{player_name}: {player_score}")
    computer_score_var.set(f"Computer: {computer_score}")
    tie_score_var.set(f"Ties: {tie_score}")
    round_number += 1
    round_var.set(f"Round: {round_number}")

    # Show streaks
    streak_msg = ""
    if player_streak > 1:
        streak_msg += f"🔥 {player_name} is on a {player_streak}-win streak! "
    if computer_streak > 1:
        streak_msg += f"💻 Computer is on a {computer_streak}-win streak! "
    if tie_streak > 1:
        streak_msg += f"🤝 Tie streak of {tie_streak}!"
    streak_var.set(streak_msg)

def show_statistics():
    total_rounds = player_score + computer_score + tie_score
    if total_rounds == 0:
        messagebox.showinfo("Statistics", "No rounds played yet!")
        return
    player_win_rate = player_score / total_rounds
    computer_win_rate = computer_score / total_rounds
    stats = f"Total Rounds Played: {total_rounds}\n"
    stats += f"{player_name}'s Win Rate: {player_win_rate:.2%}\n"
    stats += f"Computer's Win Rate: {computer_win_rate:.2%}\n"
    stats += f"{player_name}'s Longest Winning Streak: {max_player_streak}\n"

    # Overall winner
    if player_score > computer_score:
        stats += f"\n🏆 Overall Winner: {player_name} 🎉"
    elif computer_score > player_score:
        stats += "\n💻 Overall Winner: Computer 😢"
    else:
        stats += "\n🤝 Overall Result: Tie"
    messagebox.showinfo("Game Statistics", stats)

# =========================
# Buttons
# =========================

button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Snake 🐍", width=15, font=("Arial", 12), command=lambda: play_round('s')).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Water 💧", width=15, font=("Arial", 12), command=lambda: play_round('w')).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Gun 🔫", width=15, font=("Arial", 12), command=lambda: play_round('g')).grid(row=0, column=2, padx=5)
tk.Button(root, text="Show Final Statistics / End Game", font=("Arial", 12, "bold"), width=35, command=show_statistics, bg="lightblue").pack(pady=10)

# =========================
# Start GUI
# =========================
root.mainloop()