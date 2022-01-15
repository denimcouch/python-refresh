# The asterisk is the important part
# args is just a catch-all for what we pass in
# it will be collected into a tuple when the function
# is called
def multiply(*args):
  total = 1
  for arg in args:
    total = total * arg
  
  return total


def apply(*args, operator):
  if operator == '*':
    return multiply(*args)
  elif operator == '+':
    return sum(args)
  else:
    return "No valid operator provided."
  

print(apply(1,3,4,6, operator="*"))