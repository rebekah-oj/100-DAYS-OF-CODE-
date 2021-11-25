
age = input("What is your current age")

max_age = 90

years_remaining = max_age - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(message)

