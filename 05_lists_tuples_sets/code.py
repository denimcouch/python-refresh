# Lists
# Defined with [] with comma-separated values
# Maintains index of elements
list_example = ["Alex", "Karo", "Zack", "Lauren"]

# Tuples
# Defined with ()
# Tuples cannot be modified once they are created
# Maintains index of elements
tuple_example = ("Alex", "Karo", "Zack", "Lauren")

# Sets
# Defined with {}
# Sets allow you to add/remove elements, but do not allow duplicates 
# Does not care about index of elements
set_example = {"Alex", "Karo", "Zack", "Lauren"}

# Lists and Tuples can use subscript notation similar to arrays in JS or Ruby
print("Subscript notation in Lists and Tuples")
print(list_example[0])
print(tuple_example[1])

# Lists can be appended
print("Appending in lists")
list_example.append("Brian")
list_example.append("Kaylee")
print(list_example)

# Elements can be added to Sets using add()
set_example.add("Brian")
print(set_example)