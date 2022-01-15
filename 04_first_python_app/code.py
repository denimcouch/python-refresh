# Ask user for age, then respond with how many months that is
print("Age Calculator! Let me tell you how old you are in months.")

user_age = int(input("Enter your age: "))
months = user_age * 12

print(f"You're {user_age} years equates to {months} months alive on this earth.")

add_seconds = input("Would you like to know how many seconds that is? [Y/N]")
if add_seconds.lower() == 'y':
  seconds = user_age * 365 * 24 * 60 * 60
  print(f"You are {seconds} seconds old!")
else:
  print("Have a good day!")

