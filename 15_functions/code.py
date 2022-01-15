def greeting():
  print("Hello!")

greeting()

def user_age_in_seconds():
  user_age = int(input("Enter your age: "))
  age_in_seconds = user_age * 365 * 24 * 60 * 60
  print(f"You are {age_in_seconds} seconds old.")

user_age_in_seconds()

# Arguments and Parameters #
def add(x, y):
  return x + y

result = add(10, 2)
print(result)