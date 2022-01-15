class Student:
  def __init__(self, name, age, grades=[]):
    self.name = name
    self.age = age
    self.grades = grades

  def grade_average(self):
    return sum(self.grades) / len(self.grades) 


student = Student("Alex", 29, [90, 94, 92, 98, 100])

print(student.grades)
print(student.grade_average())