print("Welcome to Python Pizza Deliveries")

pizza_size = str(input("What size pizza would you prefer? Small, Medium, Large"))

add_pepperoni = str(input("Would you like pepperoni? Yes or No: "))

extra_cheese = str(input("Would you like extra cheese? Yes or No: "))

pizza = 0

if pizza_size == "Small":
    pizza += 15
    print(f"The price of a Small pizza is ${pizza}")

elif pizza_size == "Medium":
    pizza += 20
    print(f"The price of a Medium pizza is ${pizza}")
else:
    pizza += 25
    print(f"The price of a Large pizza is ${pizza}")

if add_pepperoni == "Yes":
    if pizza_size == "Small":
        pizza += 2
    else:
        pizza += 3

if extra_cheese == "Yes":
    pizza += 1
    print(f"With extra cheese, your bill is {pizza}")

