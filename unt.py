import random
import math
r=round(random.random()* 10)
attempts=0
max_attempts=3
p=print
p("im thinking of a number beween 1 and 10, you have 3  attempts to guess the number")
p(f"you have {max_attempts} guesses to reach the number")


p(r)
while attempts<max_attempts:
    guesses=int(input("enter your guess:"))
    if guesses == r:
        p("you got it!")
        break
    elif guesses>r:
        p("your number is too high")
    elif guesses<r:
        p("your number is too low")
    else:
        p("please put in a number")
    
    attempts+=1
if attempts==max_attempts:
    p(f"youre out of attempts! the correct number was {r}")

