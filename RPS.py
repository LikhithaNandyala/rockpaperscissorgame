import random
while True:
    choices=['rock','paper','scissors']
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock,paper, or scissors?:").lower()
    if player==computer:
        print(computer)
        print(player)
        print("Tie!")
    elif player=="rock":
        if computer=="paper":
            print(computer)
            print(player)
            print("You lose!")
        if computer=="scissors":
            print(computer)
            print(player)
            print("You Win!")
    elif player=="paper":
        if computer=="rock":
            print(computer)
            print(player)
            print("You Win!")
        if computer=="scissors":
            print(computer)
            print(player)
            print("You lose!")
    elif player=="scissors":
        if computer=="paper":
            print(computer)
            print(player)
            print("You Win!")
        if computer=="rock":
            print(computer)
            print(player)
            print("You lose!")
    play_again=input("Play Again? (yes/no):  ").lower()
    if play_again != "yes":
        break
print("Bye!")
