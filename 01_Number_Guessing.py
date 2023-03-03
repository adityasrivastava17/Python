import random
import math

lower=int(input("Enter lower range "))
upper=int(input("Enter upper range"))

x=random.randint(lower,upper)
print("\n You have only",
    round(math.log(upper-lower + 1,2)),
    "chances to guess the integer \n ")

count=0
while count< math.log(upper- lower +1,2):
    count +=1
    
    guess=int(input("Guess the number"))

    if x==guess:
        print("congo u guessed the number in",count , "chances")
        break

    elif x<guess:
        print("guessed too large")
    
    elif x>guess:
        print("too small")

if count>math.log(upper - lower + 1,2):
    print("You exceeded the limit of guessing")
    

