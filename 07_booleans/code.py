friends = ["Alex", "Brian"]
abroad = ["Alex", "Brian"]

# This evaluates to True since python checks that the values
# inside the lists are the same
print(friends == abroad)

# The evaluates to False since "is" is closer to a deep equivalence
# "Is" will check if friends is the same list as abroad according to memory
# not that their elements are the same
print(friends is abroad)

# This evaluates to True since both elements at the second index are the same string.
print(friends[1] is abroad[1])