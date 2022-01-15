# **kwargs is shorthand for Keyword Arguments
# it will collect all the given keyword arguments
# and put into a dictionary where the key is equal to the keyword argument given
def named(**kwargs):
  print(kwargs)


details = {
  "name": "Alex",
  "age": 29
}

# We can also use the ** to unpack a dictionary into keyword arguments
# ex: named(**details) => {'name': 'Alex', 'age': 29}


def print_nicely(**kwargs):
  named(**kwargs)
  for arg, value in kwargs.items():
    print(f"{arg}: {value}")


print_nicely(name="Alex", age=29)

# You can also use *args and **kwargs together
# This is generally used to accept any number of arguments
# Usually to pass those arguments onto another function
def both(*args, **kwargs):
  print(args)
  print(kwargs)


both(1,4,5, name="Karo", age=29)
