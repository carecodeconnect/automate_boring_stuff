# Rock Paper Scissors Game
import sys
import random
import polars as pl

print("ROCK, PAPER, SCISSORS")

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

computer_move = get_computer_move()
computer_move


wins = 0
losses = 0
ties = 0

def get_user_move():    
    print(f"{results.item(0,'wins')} Wins, {results.item(0,'losses')} Losses, {results.item(0,'ties')} Ties")
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    user_move = input('>')
    if user_move == 'q':
        sys.exit()
    return user_move

if user_move == 'r':
    computer_move = get_move()
    print("ROCK versus...") 
    print(computer_move)
    if computer_move == 'ROCK':
        print("It is a tie!")
        ties += 1
    elif computer_move == 'PAPER':
        print("You lose!")
        losses += 1
    elif computer_move == 'SCISSORS':
        print("You win!")
        wins += 1

elif user_move == 'p':
    computer_move = get_move()
    print("PAPER versus...")
    print(computer_move)
    if computer_move == 'PAPER':
        print("It is a tie!")
        ties += 1
    elif computer_move == 'SCISSORS':
        print("You lose!")
        losses += 1
    elif computer_move == 'ROCK':
        print("You win!")
        wins += 1

elif user_move == 's':
    computer_move = get_move()
    print("SCISSORS versus ..." + computer_move)
    if computer_move == 'SCISSORS':
        print("It is a tie!")
        ties += 1
    elif computer_move == 'ROCK':
        print("You lose!")
        losses += 1
    elif computer_move == 'PAPER':
        print("You win!")
        wins += 1

def win_lose_tie(user_move, computer_move, results):
    "Returns results of game"
    print(f"My move is {computer_move}")
    # Win
    if (user_move == 'r' and computer_move == 'SCISSORS') or (user_move == 'p' and computer_move == 'ROCK') or (user_move == 's' and computer_move == 'PAPER'):
        print("You win :)")
        results = results.with_columns(pl.col('wins') + 1)
        print(results)
        return results
    # Lose
    if (user_move == 'r' and computer_move == 'PAPER') or (user_move == 'p' and computer_move == 'SCISSORS') or (user_move == 's' and computer_move == 'ROCK'):
        print("You lose :(")
        results = results.with_columns(pl.col('losses') + 1)
        print(results)
        return results
    # Tie
    if (user_move == 'r' and computer_move == 'ROCK') or (user_move == 'p' and computer_move == 'PAPER') or (user_move == 's' and computer_move == 'SCISSORS'):
        print("It is a tie!")
        results = results.with_columns(pl.col('ties') + 1)
        print(results)
        return results


results
user_move
computer_move
results

def start_game():
    results = {'wins': 0, 'losses': 0, 'ties': 0}
    results = pl.DataFrame(results)
    return results

results = start_game()
user_move = get_user_move()
user_move
computer_move = get_computer_move()
computer_move
results = win_lose_tie(user_move, computer_move, results)

# Game v1
results = start_game()

for i in range(0,3):
    user_move = get_user_move()
    user_move
    computer_move = get_computer_move()
    computer_move
    results = win_lose_tie(user_move, computer_move, results)

# Game v2

def start_game():
    results = {'wins': 0, 'losses': 0, 'ties': 0}
    results = pl.DataFrame(results)
    print("Welcome to the classic game ROCK, PAPER, SCISSORS!")
    print("You will play the computer")
    print("How many games would you like to play? (e.g. 3, 5, 10)")
    games = input('>')
    return results, int(games)

results, games = start_game()
results
games

for i in range(0,games):
    user_move = get_user_move()
    user_move
    computer_move = get_computer_move()
    computer_move
    results = win_lose_tie(user_move, computer_move, results)
