print("Welcome to the rollercoaster")
height = int(input("what is your height in cm ?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5$")
    elif age <=18:
        bill = 7
        print("Youth tickets are 7$")
    else:
        bill = 12
        print("Adult ticekts are 12$")
    
    photo = input("Do you want picture taken? Y or N: ")
    if photo == "Y":
        bill += 3

    print(f"Your final bisl is {bill}")

else:
    print("Sorry you have to grow up")