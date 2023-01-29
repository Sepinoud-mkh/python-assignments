import random

words=["music","book","movie","laptop","telegram","exam"]
word=random.choice(words).lower()
guess=[]
error=0

print("The word has %d letters"%len(word))
for i in range(len(word)):
    print("-",end=" ")

while (len(guess)!=len(word)) or (error<6):
    for i in range(len(word)):
        guess_char=input("\nPlease enter your guess:")
        if guess_char in word:
            guess.append(guess_char) 
            print("The word has the letter that you guessed:",guess_char)
        else:
            guess.append("-")
            error=error+1
            print("The word doesn't have the letter that you guessed:" "-")
if guess==word:
    print("You won!!")
else:
    print("You lost!")
    print(word)