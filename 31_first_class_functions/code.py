# A first class function is essentially a variable that you can pass into arguments of other functions

def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Cannot divide by 0.")
  
  return dividend / divisor


def calculate(*values, operator):
  return operator(*values)

# Here the divide function operates as a first class function.
# By not calling the function here, we pass the value of the function to the calculate() function.
# As a result, the divide function is only called once the calculate method runs the code on line 11.
result = calculate(20,4, operator=divide)
print(result)


# Here's another example of using first class functions

def search(sequence, expected, finder):
  for elem in sequence:
    if finder(elem) == expected:
      return elem
  raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
  {"name": "Alex Mata", "age": 29},
  {"name": "Karo Cantu", "age": 29},
  {"name": "Brian Gallagher", "age": 29},
  {"name": "Kaylee Gallagher", "age": 29},
]

def get_friend_name(friend):
  return friend["name"]


print(search(friends, "Alex Mata", get_friend_name))
