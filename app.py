# Initial Welcome Message
print("Welcome to my GitHub Project Python program!")
# Checks how much food was eaten today, user input prompt
food = input("How many meals did you eat today? ")
# Meal calculation based on user input
meals = float(food)
daily_meals = meals * 7
# Formatted output displayed here
print(f"You are on track to eat {daily_meals} meals this week.")
# Simple error handling for my meals program
try:
    meals = float(food)
except ValueError:
    print("Please enter a valid number.")
    exit()