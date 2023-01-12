import random

player_Score=0
computer_Score=0
a=0
Options=["rock","paper","scissors"]

print("Hi!\nWelcome to the Rock,Paper,Scissors game.")
name=input("Please enter your name:")

print("What is your choice?")
while(player_Score!=5 and computer_Score!=5):
    choice_Player=str(input("rock? or paper? or scissors?"))
    choice_Computer=random.choice(Options)
    if (choice_Player=="rock" and choice_Computer=="scissors") or (choice_Player=="paper" and choice_Computer=="rock") or (choice_Player=="scissors" and choice_Computer=="paper"):
        player_Score=player_Score+1
    elif (choice_Player=="paper" and choice_Computer=="scissors") or (choice_Player=="scissors" and choice_Computer=="rock") or (choice_Player=="rock" and choice_Computer=="paper"):
        computer_Score=computer_Score+1
    elif choice_Player==choice_Computer:
        print("Try again!")
    print("\nComputer choice was:%s"%choice_Computer) 
    print("Your choice was:%s"%choice_Player)
    print("Computer score is:%.d"%computer_Score)
    print("Your score is:%.d"%player_Score)
    a=a+1
    if player_Score=="5" or computer_Score=="5":
        break
if player_Score>computer_Score:
    print("Congratulations,%s you won!!!"%name)
else:
    print("Unfortunatelly you lost :((\n")
