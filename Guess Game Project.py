secret_word = "Python"
guess = ""
guess_count =0
guess_limit = 3
check_guess = False
while guess != secret_word and not check_guess:
    if guess_count < guess_limit:
        guess = input("Guess the word: ")
        guess_count+=1
    else:
        check_guess = True

if check_guess:
    print("you lose")
else:
    print("you win")


    
