import string
import random
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def gen_pass():
    pass_length =  int(input("How long would you like your password to be:  "))
    random.shuffle(characters)
    password = []
    for x in range(pass_length):
        password.append(random.choice(characters))

    random.shuffle(characters)
    password = "".join(password)
    print(password)

option = input("Do you want to generate a password?  Yes or No : ")
if option =="Yes":
    gen_pass()
elif option =="No":
    print("Exiting the program...")
    quit()
else:
    print("Invalid option, please enter Yes or No")
    quit()

#Ask user if they want to generate a password or not
#if yes, ask for password length
#generate password
# print password
#if not want to generate a password then exit program