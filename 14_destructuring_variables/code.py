# Python reads this as a tuple
t = 5, 11

# We can destructure t like this
# x = 5 and y = 11 here
x, y = t

student_attendance = {
  "Alex": 86,
  "Brian": 98,
  "Zack": 95
}

# This will create a list of tuples with the values equal
# to the key/value pairs
# eg: [('Alex', 86), ('Brian', 98), ('Zack', 95)]

# student_attendance_list = list(student_attendance.items())
# for student in student_attendance_list:
#   name, attendance = student
#   print(f"{name}: {attendance}")

# That is why we can do the following to destructure instead
for name, attendance in student_attendance.items():
  print(f"{name}: {attendance}")

# Let's get the name and role from this tuple
person = ("Karo", 29, "Software Engineer")

# The underscore is the pythonic way to ignore an element while destructuring
name, _, profession = person

# The second variable collects all the other values when destructuring
# eg: head = [1] tail = [2, 3, 4]
head, *tail = [1, 2, 3, 4]