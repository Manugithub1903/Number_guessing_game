
def chances(level):
    if level=="hard":
        return 5
    else:
        return 10


import  random
a=random.randint(1,100)
print("Hello! Welcoime to the  'NUMBER GUESSING' game")
print(""" Choose The Mode
          Easy: You have 10 chances for guess the number
          Hard: You have  5 chances to guess the number""")
level=input("Choose the level:1.Easy,2.Hard (Type easy or hard)\n").lower()
turns=chances(level)

count=1
while turns!=0:
     guess=int(input("Guess the number between 1 to 100.!\n"))
    #  result(a,guess)
     if a==guess :
        print(f"Congrates:'You have win in {count} turns")
        break
     elif(a>guess):
        print("Guess high number")
     else:
        print("Guess low number")
     if turns==1:
        print("Sorry! You have lose the game")
     turns-=1
     count+=1

