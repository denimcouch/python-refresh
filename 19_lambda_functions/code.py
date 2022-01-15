# A lambda function is a nameless function that only returns values
# They are meant to be short functions that are often used without a name
# Lambdas are mostly single line for readability
# Best practices are to usually define are normal function as opposed to a lambda

# Ex: an addition lambda
print((lambda x, y: x + y)(1,2))

# Here's an actual use case

sequence = [1, 3, 5, 9]
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
