import random 

someWords = ["apple", "banana", "mango", "strawberry",
"orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon",
"cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]

word=random.choice(someWords)

print("Guess the letter")

guesses=" "

turns=len(word)+2

while(turns>0):
    guess=input("Enter the letter")
    guesses+=guess
    fail=0
    for i in word:
        if i in guesses:
            print(i,end=" ")
        else:
            print("_")
            fail+=1

    
    
    if fail==0:
        print("You Win")
        print("The Word is ",word)
        break

    

    if guess not in word:
        turns-=1
        print("wrong")
        print("you have ", +turns, "left")
        if (turns==0):
            print("You Lose")
    
    
