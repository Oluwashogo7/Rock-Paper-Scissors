import random

while True:
    user_action = input("R(for Rock) or P(for Paper) or S(Scissors): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    if user_action == "R" or user_action == "S" or user_action == "P":
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    else :
        print("Wrong Input")
   
    if user_action == computer_action :
        print("Yikes, it's a tie. Play again.")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors. You win!")
        else :
            print("Paper covers rock. Computer wins!")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts papaer. You win!")
        else :
            print("Rock smashes scissors. Computer wins!")
    elif user_action == "P":
        if computer_action == "R":
            print("paper covers rock. You win!")
        else :
            print("Scissors cuts paper. Computer wins!")
    play_again = input("Wanna play again? Yes or No: ")
    if play_again == "No":
        break        
