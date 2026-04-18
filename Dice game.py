import random

def play_game():
    print("Welcome to Dice Game ")
    
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")
    
    score1 = 0
    score2 = 0
    
    for i in range(1, 4):
        print("\n--- Round", i, "---")
        
        input(player1 + " press Enter to roll dice...")
        dice1 = random.randint(1, 6)
        print(player1, "got:", dice1)
        score1 += dice1
        

    print("Final Scores:")
    print(player1, "=", score1)


    for i in range(1, 4):
        print("\n--- Round", i, "---")
        input(player2 + " press Enter to roll dice...")
        dice2 = random.randint(1, 6)
        print(player2, "got:", dice2)
        score2 += dice2


    print("Final Scores:")
    print(player2, "=", score2)


    if score1 > score2:
        print("Winner is", player1)
    elif score2 > score1:
        print("Winner is", player2)
    else:
        print("It's a Draw!")
play_game()