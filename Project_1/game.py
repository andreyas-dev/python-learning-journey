# Snake Water Gun Game
'''snake = 1
water = -1
 gun = 0'''
import random, time, os

def play_again():
    while True:
        play_again_input = input("Do you want to play again? (Y/N): ").strip().lower()
        if play_again_input not in ['y', 'n']:
            print("Invalid Input! Please enter Y/y for yes and N/n for no")
        elif play_again_input != 'y':
            print("Thanks for playing!")
            return False
        else:
            return True


player_score = 0
computer_score = 0
tie_score = 0
round_number = 1

print("=============================== \nWelcome to Snake Water Gun Game\n===============================")
print("Enter your choice: S for Snake, W for Water, G for Gun")


while True:
    print(f"\n===============================\nRound {round_number}\n===============================")
    user = input("Enter your choice: ").strip().lower()

    while user not in ['s', 'w', 'g']:
        print("Invalid input! Please enter S/s for snake, W/w for water and G/g for gun")
        user = input("Enter your choice: ").strip().lower()

    computer = random.choice([1, -1, 0])
    user_dict = {'s': 1, 'w': -1, 'g': 0}
    reverse_dict = {1: 's', -1: 'w', 0: 'g'}
    user_value = user_dict[user]

    words = {'s': 'Snake 🐍', 'w': 'Water 💧', 'g': 'Gun 🔫'}
    print("\n===============================\nComputer choosing....\n===============================\n")
    time.sleep(1)

    print(f"Computer choose: {words[reverse_dict[computer]]}\nYou choose: {words[reverse_dict[user_value]]}")

    if computer == user_value:
        tie_score += 1
        print(f"\n==============\nIt's a tie!\n==============\n")
        if not play_again():
            break
    else:
        if computer - user_value == 1 or computer - user_value == -2:
            computer_score += 1
            print(f"\n===================================\n{words[reverse_dict[computer]]} beats {words[reverse_dict[user_value]]}! You lose! 😢\n===================================\n")
            print("Better luck next time!")
            if not play_again():
                break
        else:
            player_score += 1
            print(f"\n===================================\n{words[reverse_dict[user_value]]} beats {words[reverse_dict[computer]]}! You Win! 🎉\n===================================\n")
            print("Congratulations!")
            if not play_again():
                break
    round_number += 1
    print(f"Current Scores:\nPlayer: {player_score}\nComputer: {computer_score}\nTies: {tie_score}")
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

os.system('cls' if os.name == 'nt' else 'clear')
print(f"\n===============================\nFinal Scores:\nPlayer: {player_score}\nComputer: {computer_score}\nTies: {tie_score}\n===============================")

if player_score > computer_score:
    print("Congratulations! You are the overall winner! 🎉")
elif computer_score > player_score:
    print("Computer wins overall! Better luck next time! 😢")
else:
    print("It's an overall tie! Great game! 🤝")














# Simple Logics
'''if(computer == 1 and user == -1):  1-(-1) = 2
        print("You lose!")

    elif(computer ==1 and user == 0): 1-0 = 1
        print("You Win!")

    elif(computer == -1 and user == 1):-1-1 = -2
        print("You Win!")

    elif(computer ==-1 and user == 0): -1-0 = -1
        print("You lose!")

    elif(computer == 0 and user == 1): 0-1 = -1
        print("You lose!")

    elif(computer == 0 and user == -1): 0-(-1) = 1
        print("You Win!")
'''