print("Welcome to the roller coaster!")

height = int(input("What is your height in cm?"))

age = int(input("How old are you? "))

photos = str(input("Do you want photos?, type yes or no"))

if height >= 120:
    print("you can ride the roller coaster!!")
    if age < 12:
        bill = 5
        print(f"and your ride fee is {bill}")

    elif age <= 18:
        bill = 18
        print(f" and your ride fee is {bill}")

    else:
        bill = 12
        print(f"your ride fee is {bill}")

    if photos == "yes":
        bill += 3
        print(f"with photos, your final bill is {bill}")

    else:
        print(f"your final bill is {bill}")
else:
    print("You are too short to go on the ride.")
