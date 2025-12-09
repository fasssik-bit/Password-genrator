import random
import string
def genrate_passoward(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passoward = ""
    for i in range(length):
        passoward += random.choice(characters)
    return passoward
    # main program
print("welcome to fasih's passoward generator")
length=int(input("enter your desired passoward length:"))
final_passoward= genrate_passoward(length)
print("your passowrd generated is :",final_passoward)
