import math
import random

#mastermind

#intro

length = int(input("WELCOME TO MASTERMIND\nLength: "))

#create a random set of numbers

mid = random.randrange(10 ** (length - 1),10 ** (length))

#guess the numbers

yeat = int(input("MAKE YOUR GUESS:\n"))

if yeat == mid:
    print("Wow. You got it in one. Congrats.")
    
#correct or incorrect? loop if incorrect

else:
    
    while (yeat != mid):
        mark = 0
        
        yeat = str(yeat)
        mid = str(mid)
        
        c = ['X'] * length
        
        for i in range(0,length):
            if mid[i] == yeat[i]:
                mark += 1
                c[i] = yeat[i]
            else:
                continue
            
        if (mark < 4) and (mark != 0):
            print("Not Quite! You did get", mark, "digits correct.")
            
            for k in c:
                print(k, end = ' ')
                
            print("\n")
            yeat = int(input("Make Your Next Guess:\n"))
        
        elif(mark == 0):
            print("Not Even Close!")
            yeat = int(input("Make Your Next Guess:\n"))
        
    if yeat == mid:
        print("That's It!")
        print("Only Took You", mark, "Tries!")




#congratulations

print(mid)
