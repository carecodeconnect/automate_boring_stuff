# Rock Paper Scissors Game

import sys
import random
import polars as pl

def start_game():
    "Initialises variables and gets number of games to play"
    results = {'wins': 0, 'losses': 0, 'ties': 0}
    results = pl.DataFrame(results)
    print("Welcome to the classic game ROCK, PAPER, SCISSORS!")
    print("You will play the computer")
    print("How many games would you like to play? (e.g. 3, 5, 10)")
    games = input('>')
    return results, int(games)

def get_user_move():    
    print(f"{results.item(0,'wins')} Wins, {results.item(0,'losses')} Losses, {results.item(0,'ties')} Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    user_move = input('>')
    if user_move == 'q':
        sys.exit()
    return user_move

def get_computer_move():
    move_int = random.randint(1, 3)
    if move_int == 1:
        move_str = "ROCK"
        return move_str
    elif move_int == 2:
        move_str = "PAPER"
        return move_str
    elif move_int == 3:
        move_str = "SCISSORS"
        return move_str

def win_lose_tie(user_move, computer_move, results):
    "Returns results of game"
    print(f"My move is {computer_move}")
    # Win
    if (user_move == 'r' and computer_move == 'SCISSORS') or (user_move == 'p' and computer_move == 'ROCK') or (user_move == 's' and computer_move == 'PAPER'):
        print("You win :)")
        results = results.with_columns(pl.col('wins') + 1)
        #print(results)
        return results
    # Lose
    if (user_move == 'r' and computer_move == 'PAPER') or (user_move == 'p' and computer_move == 'SCISSORS') or (user_move == 's' and computer_move == 'ROCK'):
        print("You lose :(")
        results = results.with_columns(pl.col('losses') + 1)
        #print(results)
        return results
    # Tie
    if (user_move == 'r' and computer_move == 'ROCK') or (user_move == 'p' and computer_move == 'PAPER') or (user_move == 's' and computer_move == 'SCISSORS'):
        print("It is a tie!")
        results = results.with_columns(pl.col('ties') + 1)
        #print(results)
        return results

results, games = start_game()

for i in range(0,games):
    user_move = get_user_move()
    user_move
    computer_move = get_computer_move()
    computer_move
    results = win_lose_tie(user_move, computer_move, results)

print(results)

if (int(results.item(0,'wins')) > int(results.item(0,'losses'))) & (int(results.item(0,'wins'))) > (int(results.item(0,'ties'))):
    print("You won overall!!!")
elif (int(results.item(0,'losses')) > int(results.item(0,'wins'))) & (int(results.item(0,'losses'))) > (int(results.item(0,'ties'))):
    print("You lost overall :'(")
elif (int(results.item(0,'ties')) > int(results.item(0,'wins'))) & (int(results.item(0,'ties'))) > (int(results.item(0,'losses'))):
    print("We tied overall!")

print("Thank you for playing with me!")