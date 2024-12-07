#import random
# define a function to roll the dice
# create a dictionary that will have the drawings of the dice
import random
def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),}

    roll = input("Wanna Roll the Dice?? (Yes/No): ")

    while roll.lower()=="Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll = input("Wanna Roll Again?? (Yes/No): ")

roll_dice()
