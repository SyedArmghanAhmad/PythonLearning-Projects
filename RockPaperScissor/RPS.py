import random

exit =  False
score_user = 0
score_pc = 0

while exit  == False:
    options = ["rock","paper","scissors"]
    user_choice = input("Choose rock, paper, scissors or exit: ")
    computer_choice = random.choice(options)

    if user_choice == "exit" :
        print("Game ended")
        print("You won a total score of "+str(score_user)+" and the computer'score is "+str(score_pc))
        exit = True

    if user_choice == "rock":
        if computer_choice == "rock":
            print("Your input is Rock")
            print("Computer's input is Rock")
            print("It is a tie!")
        elif computer_choice == "paper":
            print("Your input is Rock")
            print("Computer's input is paper")
            print("You lose!")
            print("Computer wins!")
            score_pc += 1
        elif computer_choice == "scissors":
            print("Your input is Rock")
            print("Computer's input is scissors")
            print("You win!")
            score_user += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Your input is paper")
            print("Computer's input is Rock")
            print("You win!")
            score_user +=1
        elif computer_choice == "paper":
            print("Your input is paper")
            print("Computer's input is paper")
            print("It is a tie!")
        elif computer_choice == "scissors":
            print("Your input is Paper")
            print("Computer's input is Scissors")
            print("Computer wins!")
            score_pc +=1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("Your input is scissors")
            print("Computer's input is Rock")
            print("Computer wins!")
            score_pc +=1
        elif computer_choice == "paper":
            print("Your input is scissors")
            print("Computer's input is paper")
            print("You win!")
            score_user += 1
        elif computer_choice == "scissors":
            print("Your input is scissors")
            print("Computer's input is scissors")
            print("It is a tie!")



    elif user_choice not in options and user_choice != "exit":
        print("Invalid input. Please try again.")

