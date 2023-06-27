#create a simple reward system
#user any number  1 - 5
#they are rewarded

bettingnum = int(input("Enter any number between 1 to 5"))

if bettingnum == 1:
    print("you have won a cow")
elif bettingnum == 2:
    print("you have won a car")

elif bettingnum == 3:
    print("you have won a goat")
elif bettingnum == 4:
    print("you have won a cat")
elif bettingnum ==  5:
    print("you have won a house")
else:
    print("Invalid Number entered")