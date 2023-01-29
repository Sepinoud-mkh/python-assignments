import random

words=["music","book","movie","laptop","telegram","exam"]
word=random.choice(words).lower()
true_Guess=[]
guess=[]
error=0
i=0

print("The word has %d letters"%len(word))
for i in range(len(word)):
    print("-",end=" ")

while(len(true_Guess)!=len(word) and error<6):
    guess_char=input("\nPlease enter your guess:")
    if guess_char in word:
        print("The word has the letter that you guessed:",guess_char)
        i=word.index(guess_char)
        true_Guess[i]=guess_char
    else:
        guess.append("-")
        error=error+1
        print("The word doesn't have the letter that you guessed:" "-")
if true_Guess==word:
    print("You won!!")
    print(true_Guess)
elif(error==6):
    print("You lost!")
    print(word)