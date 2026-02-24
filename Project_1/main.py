# =========================================================
# 🎮 Snake Water Gun Game (CLI Version)
# ---------------------------------------------------------
# A fun and interactive terminal-based Snake Water Gun game
# built with Python. Features colored output, score tracking,
# win streaks, and smooth user interaction.
#
# 👤 Author: Andreyas
# 🐍 Language: Python (3.14)
# 💻 Platform: Terminal / Command Line
# 🔢 Version: v1.0
# =========================================================

# snake = 1
# water = -1
# gun = 0

import random
import time
import os

# =========================
# Helper Functions
# =========================

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def colored(text, color_code):
    """Return colored text using ANSI escape codes."""
    return f"\033[{color_code}m{text}\033[0m"

def get_user_choice():
    """Get validated user input (s/w/g or full words)."""
    while True:
        choice = input("Enter your choice (S/s for Snake, W/w for Water, G/g for Gun): ").strip().lower()
        if choice in ['s', 'snake']:
            return 's'
        elif choice in ['w', 'water']:
            return 'w'
        elif choice in ['g', 'gun']:
            return 'g'
        else:
            print(colored("Invalid input! Please enter S/s, W/w, or G/g.", "91"))  # red

def get_computer_choice():
    """Randomly select computer choice."""
    return random.choice([1, -1, 0])

def determine_winner(user_val, comp_val):
    """Determine winner based on numeric values."""
   
    # Simple Logics
    # if(computer == 1 and user == -1):  1-(-1) = 2
    #     print("You lose!")
    #
    # elif(computer ==1 and user == 0): 1-0 = 1
    #     print("You Win!")
    #
    # elif(computer == -1 and user == 1):-1-1 = -2
    #     print("You Win!")
    #
    # elif(computer ==-1 and user == 0): -1-0 = -1
    #     print("You lose!")
    #
    # elif(computer == 0 and user == 1): 0-1 = -1
    #     print("You lose!")
    #
    # elif(computer == 0 and user == -1): 0-(-1) = 1
    #     print("You Win!")

    if user_val == comp_val:
        return 'tie'
    elif comp_val - user_val == 1 or comp_val - user_val == -2:
        return 'computer'
    else:
        return 'player'

def play_again():
    """Ask user if they want to play again"""
    choice = input("Do you want to play again? (Y/N): ").strip().lower()
    if choice not in ['y', 'n']:
        print(colored("Invalid Input! Please enter Y/y for yes and N/n for no.", "91"))
        return play_again()  # recursive call
    return choice == 'y'

def countdown(text="Computer is choosing"):
    """Add suspense"""
    print(text, end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

# =========================
# Main Game
# =========================

# Initialize scores and streaks
player_score = 0
computer_score = 0
tie_score = 0
round_number = 1
player_streak = 0
computer_streak = 0
tie_streak = 0
max_player_streak = 0

# Mapping dictionaries
user_dict = {'s': 1, 'w': -1, 'g': 0}
reverse_dict = {1: 's', -1: 'w', 0: 'g'}
words = {'s': 'Snake 🐍', 'w': 'Water 💧', 'g': 'Gun 🔫'}

# Welcome message
print("="*40)
print(colored("Welcome to Snake Water Gun Game 🎮", "96"))  # cyan
print("="*40)

print("-"*40)
print(colored("               Game Rules           ", "35"))  #
print("-"*40)
print("1.  Snake drinks Water.\n2.  Water douses Gun.\n3.  Gun kills Snake.")
print("-"*40)
input(colored(f"           Press Enter to Start           \n{"-"*40}", "33"))  #

player = input("Enter your name:").strip().capitalize()
while True:
    print(colored(f"\n========== ROUND {round_number} ==========", "94"))  # blue
    user_choice = get_user_choice()
    user_value = user_dict[user_choice]

    comp_value = get_computer_choice()

    countdown()

    # Show choices
    print(f"Computer chose: {words[reverse_dict[comp_value]]}")
    print(f"You chose: {words[user_choice]}")

    # Determine winner
    winner = determine_winner(user_value, comp_value)

    if winner == 'tie':
        tie_score += 1
        tie_streak += 1
        player_streak = computer_streak = 0
        print(colored("It's a tie! 🤝", "93"))  # yellow
    elif winner == 'player':
        player_score += 1
        player_streak += 1
        if player_streak > max_player_streak:
            max_player_streak = player_streak

        computer_streak = tie_streak = 0
        print(colored(f"{words[user_choice]} beats {words[reverse_dict[comp_value]]}! You Win! 🎉", "92"))  # green
    else:
        computer_score += 1
        computer_streak += 1
        player_streak = tie_streak = 0
        print(colored(f"{words[reverse_dict[comp_value]]} beats {words[user_choice]}! You lose! 😢", "91"))  # red

    # Show current scores & streaks
    print("\n" + "-"*30)
    print(f"Scores -> {player}: {player_score} | Computer: {computer_score} | Ties: {tie_score}")
    if player_streak > 1:
        print(colored(f"🔥 {player} is on a {player_streak}-win streak!", "92"))
    if computer_streak > 1:
        print(colored(f"💻 Computer is on a {computer_streak}-win streak!", "91"))
    if tie_streak > 1:
        print(colored(f"🤝 Tie streak of {tie_streak}!", "93"))
    print("-"*30)

    round_number += 1

    # Ask to play again
    if not play_again():
        break

    clear_screen()

# Final Scores
clear_screen()
print(colored("\n=================== FINAL SCORES ===================", "96"))
print(f"{player}: {player_score} | Computer: {computer_score} | Ties: {tie_score}")
print("="*50)

total_round = player_score + computer_score + tie_score
player_win_rate = (player_score/total_round)
Computer_win_rate = (computer_score/total_round)


print(colored(f"\n=================== {player}'s Game Statistics ===================", "96"))
print(f"Total rounds played : {total_round}")
print(f"{player}'s Win rate : {player_win_rate:.2%}")
print(f"Computer's Win rate : {Computer_win_rate:.2%}")
print(f"{player}'s longest winning streak is : {max_player_streak}")
print("="*50)

# Declare overall winner
if player_score > computer_score:
    print(colored(f"\n🏆 Congratulations! You are the overall winner! {player} 🎉", "92"))
elif computer_score > player_score:
    print(colored("\n💻 Computer wins overall! Better luck next time! 😢", "91"))
else:
    print(colored("\n🤝 It's an overall tie! Great game!", "93"))