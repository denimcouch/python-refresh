friends = [
  {
    "name": "Alex",
    "age": 29
  },
  {
    "name": "Zack",
    "age": 29
  },
  {
    "name": "Brian",
    "age": 29
  },
]

for friend in friends:
  print(f"{friend['name']} is {friend['age']} years old.")

student_attendance = {
  "Alex": 86,
  "Brian": 98,
  "Zack": 95
}

for student, attendance in student_attendance.items():
  print(f"{student}: {attendance}")

attend_vals = student_attendance.values()

print(sum(attend_vals))