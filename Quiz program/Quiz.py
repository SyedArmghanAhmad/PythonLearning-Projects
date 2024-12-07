#a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key value pairs
#display each question to the user and allow them to answer
# tell them if they answer right or wrong
# show the final result when quiz is completed

quiz ={
    "Question1":{
    "Question":"What is the Capital of Pakistan?",
    "Answer": "Islamabad"
    },
    "Question2":{
    "Question":"What is the square root of 144?",
    "Answer": "12"
    },
    "Question3":{
    "Question":"What is the capital city of Canada?",
    "Answer": "ottawa"
    },
    "Question4":{
    "Question":"What is the tallest building in the world?",
    "Answer": "Burj Khalifa"
    },
    "Question5":{
    "Question":"What is the chemical symbol for gold?",
    "Answer": "AU"
    },
    "Question6":{
    "Question":" Which planet is known as the Red Planet?",
    "Answer": "Mars"
    },
}

score = 0

for key, value in quiz.items():
    print(value["Question"])
    answer = input("Answer: ")
    if answer.lower() == value['Answer'].lower():
        print("Correct!😄")
        score +=1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong 😥")
        print("The Answer is: " + value['Answer'])
        print("Your score is: " + str(score))
        print("")
        print("")


print("Your Final Score is: " + str(score) + " our of 6 questions correctly")
print("Your percentage is " + str(score/6*100) + "%")

