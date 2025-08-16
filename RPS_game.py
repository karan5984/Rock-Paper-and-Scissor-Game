import random
def botRPSgame():
    bot = random.choice(choice)
    while True:
        player = input("\nEnter your choice: ")
        if player not in list:
            print("Invalid Input!!! Please try again.")
        else:
            random.shuffle(choice)
            p_choice = choice[int(player) - 1]
            break
    print("\nResult:")
    if p_choice == "Scissor" and bot == "Paper":
        print(f"Congratulations! Player wins for {p_choice} over bot's {bot}!")
    elif p_choice == "Paper" and bot == "Rock":
        print(f"Congratulations! Player wins for {p_choice} over bot's {bot}!")
    elif p_choice == "Rock" and bot == "Scissor":
        print(f"Congratulations! Player 1 wins for {p_choice} over bot's {bot}!")
    elif p_choice == bot:
        print(f"Draw for both {p_choice} choice.")
    else:
        print(f"Congratulations! Bot wins for {bot} over Player's {p_choice}")
def RPSgame():
    while True:
        player1 = input("\nEnter player 1 choice: ")
        if player1 not in list:
            print("Invalid Input!!! Please try again.")
        else:
            random.shuffle(choice)
            p1_choice = choice[int(player1) - 1]
            break
    while True:
        player2 = input("Enter player 2 choice: ")
        if player2 not in list:
            print("Invalid Input!!! Please try again.")
        else:
            random.shuffle(choice)
            p2_choice = choice[int(player2) - 1]
            break
    print("\nResult:")
    if p1_choice == "Scissor" and p2_choice == "Paper":
        print(f"Congratulations! Player 1 wins for {p1_choice} over player 2's {p2_choice}!")
    elif p1_choice == "Paper" and p2_choice == "Rock":
        print(f"Congratulations! Player 1 wins for {p1_choice} over player 2's {p2_choice}!")
    elif p1_choice == "Rock" and p2_choice == "Scissor":
        print(f"Congratulations! Player 1 wins for {p1_choice} over player 2's {p2_choice}!")
    elif p1_choice == p2_choice:
        print(f"Draw for both players {p1_choice} choice.")
    else:
        print(f"Congratulations! Player 2 wins for {p2_choice} over Player 1's {p1_choice}")
while True:
    mode = int(input("\nModes:\n1. Single player\n2. Multiplayer\n3. Exit\n\nChoose mode: "))
    if( mode == 1):
        choice = ["Rock", "Paper", "Scissor","Rock", "Paper", "Scissor","Rock", "Paper", "Scissor"]
        print("\nEnter number from 1 to 9 to randomly choose your choice from Rock, Paper and Scissor.")
        list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        botRPSgame()
        while True:
            print("\nDo you want to play again ?")
            again = str(input("Enter 'y' for yes and 'n' for no: "))
            if again == "y" or again == "Y":
                botRPSgame()
            elif again == "n" or again == "N":
                print("Thanks for playing :)")
                break
            else:
                print("Invalid Input!!! Please try again.")
    elif (mode == 2):
        choice = ["Rock", "Paper", "Scissor","Rock", "Paper", "Scissor","Rock", "Paper", "Scissor"]
        print("\nEnter number from 1 to 9 to randomly choose your choice from Rock, Paper and Scissor.")
        list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        RPSgame()
        while True:
            print("\nDo you want to play again ?")
            again = str(input("Enter 'y' for yes and 'n' for no: "))
            if again == "y" or again == "Y":
                RPSgame()
            elif again == "n" or again == "N":
                print("Thanks for playing :)")
                break
            else:
                print("Invalid Input!!! Please try again.")
    elif (mode == 3):
        print("...")
        break
    else:
        print("Invalid Input! Try again.")
