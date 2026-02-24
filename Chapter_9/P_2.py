''' game() function in a program lets a user to play a game and return score
as integer.You need to read a file High_score.txt which is either blank or 
contain previous high score.you need to write a program to write a High score
when the game() function or User breaks the High score. '''

import random
def game():
    print("You are playing a game...")
    score = random.randint(1,50)
    
    with open("hi_score.txt","r") as f:
        hi_score = f.read()

        if(hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0
        
    print(f"Your Score: {score}")

    if(score > hi_score):
       with open("hi_score.txt", "w") as f:
            f.write(str(score))

    return score
    

game()
