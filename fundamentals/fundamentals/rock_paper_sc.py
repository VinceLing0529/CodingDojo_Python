

import random
my_choice= input('Rock, Paper, Scissors :') # input takes a prompt, which needs to be a string

all=["rock","paper","scissors"]
if my_choice.lower() not in all:
    print("not valid")
else:
    ran = random.choice(all)
    print("The computer select {}".format(ran))
    if ran == my_choice.lower():
        print("draw")
    if my_choice.lower()=="rock":
        if ran=="paper":
            print ('you lose')
        if ran=="scissors":
            print ("you won")
    if my_choice.lower()=="paper":
        if ran=="rock":
            print ("you won")
        if ran=="scissors":
            print ('you lose')
    if my_choice.lower()=="scissors":
        if ran=="rock":
            print ('you lose')
        if ran=="paper":
            print ("you won")
