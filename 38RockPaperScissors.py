# 38. Rock papaer scissors[03:10:35]-----------------------------------------------------
import random
while True:
    choices = ["rock","paper","scissors"]
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock, paper or scissors?: ").lower()

    if player==computer: 
        print("Computer:" + computer) 
        print("Player: "+player)
        print("Tie!!")
    elif player=="rock":
        if computer=="paper":
            print("Computer:" + computer) 
            print("Player: "+player)
            print("Computer Won!!!")
        elif computer=="scissors":
            print("Computer:" + computer) 
            print("Player: "+player)
            print("Player Won!!!")
    elif player=="paper":
        if computer=="rock":
            print("Computer:" + computer) 
            print("Player: "+player)
            print("Player Won!!!")
        elif computer=="scissors":
            print("Computer:" + computer) 
            print("Player: "+player)
            print("Computer Won!!!")
    else:
        if computer=="rock":
            print("Computer:" + computer) 
            print("Player: "+player)
            print("Computer Won!!!")
        elif computer=="paper":
            print("Computer:" + computer) 
            print("Player: "+player)
            print("Player Won!!!")
    play_again=input("Play again?: (yes/no):  ").lower()
    if play_again!='yes':
        break
print("Bye! Looser")