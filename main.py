# A project that mimicks the game of Rock-Paper-Scissors # 
#   - options
import random

# list valid options
options = ['r', 'p', 's']
print("\nHi there! Would you play a game of Rock-Paper-Scissors with me?\n\
    Use 'R' for Rock, 'P' for Paper and 'S' for Scissors")
print("\n**Thanks, now let's play. Only valid letters apply**")

# prompt fro user input and allow the computer play
def play():
    global player, computer
    player = input("\nReady? => Rock...Paper...Scissors. PLAY!: ").lower()
    computer = random.choice(options).lower()

play()

# DEfine the game rules    
def rules():
    while player not in options:
        print('   [Oops!...please enter a valid letter]')
        play()
    else:
        print('Player ({}) : Computer: ({}) '.format(player.upper(), computer.upper()))

    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        print('Congrats, You Win!')
    elif (player == 'r' and computer == 'r') or (player == 's' and computer == 's') or (player == 'p' and computer == 'p'):
        print('Oops, we got a tie. We replay again')
        play()
        rules()
    else:
        print('Tadaa!, CPU wins....')

rules()