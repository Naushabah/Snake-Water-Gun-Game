import random
'''
1 for snake 
2 for water 
3 for gun
'''
computer=random.choice([1,2,3])
youstr=input("Enter your choice\n")

youdict={"Snake" : 1 , "Water" : 2 , "Gun" : 3}
reversedict={1 : "Snake", 2 : "Water", 3 : "Gun" }
you=youdict[youstr]
print(f" You chose {reversedict[you]}\n Computer chose {reversedict[computer]}")

if(computer==you):
    print("Its a Draw")
else:
    if(computer==1 and you==2):
        print("You Lose")
    elif(computer==1 and you==3):
        print("You Win")
    elif(computer==2 and you==1):
        print("You win")
    elif(computer==2 and you==3):
        print("You Lose")
    elif(computer==3 and you==2):
        print("You Win")
    elif(computer==3 and you==1):
        print("You Lose")
    else:
        print("Something went wrong")