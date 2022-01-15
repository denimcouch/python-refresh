def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Cannot divide by 0.")
  
  return dividend / divisor


grades = [87, 92, 98, 99, 100]

try:
  average = divide(sum(grades), 0)
except ZeroDivisionError as e:
  print(e)
  print("You have no grades yet.")
else:
  print(f"Your average grade is {average}.")
