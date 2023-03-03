import random

a=input("Enter your name")
print(f"Good Luck! {a}")

words=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word=random.choice(words)

print("Guess the characters")
 
guesses = ''

turns=12

while(turns>0):

    failed=0
    for i in word:
        if i in guesses:
            print(i,end=" ")
        else:
            print("_")
            failed+=1
    
    if failed==0:
        print("You Win")
        print("the word is ",word)
        break

    guess=input("guess a character")
    guesses+=guess

    if guess not in word:
        turns-=1
        print("wrong")
        print("you have ", +turns, " more turns left" )
        if (turns==0):
            print("You Lose")

