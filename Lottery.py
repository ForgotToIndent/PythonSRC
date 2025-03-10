import random

print("--------------------------------")
print("LOTTERY LOTTERY LOTTERY LOTTERY")
print("--------------------------------")

# Code to generate a random lottery number between 0 and 99
lottery = random.randint(0, 99)
# Formatting the random generated number as two digits
lotteryStr = f"{lottery:02d}"

#user input to enter a number between 0 and 99
user_input = input("Enter your lottery pick (two digits between 0 and 99): ")
# Format the user input as two digits
user_str = f"{int(user_input):02d}"

#if else statements to check for matches
if user_str == lotteryStr:
    print("Exact Match! You win 10,000")
elif sorted(user_str) == sorted(lotteryStr):
    print("The digits match! You win 3000")
elif (user_str[0] in lotteryStr) or (user_str[1] in lotteryStr):
    print("One digit matched! You win 1000.")
else:
    print("No matches, You Lost!")

#Display the lottery numbers and the user picked numbers
print(f"The lottery number was: {lotteryStr}")
print(f"Your number was: {user_str}")
