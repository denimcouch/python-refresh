class Person:
  def __init__(self, name, age, hobbies=[]):
    self.name = name
    self.age = age
    self.hobbies = hobbies

  # The __str__ method is used to display useful info
  # about an object in string format
  def __str__(self):
    return f"Person {self.name}, {self.age} years old."

  # The __repr__ method is mean to display a info
  # about an object that could be useful for devs
  def __repr__(self):
    return f"<Person Object('{self.name}', {self.age}, {self.hobbies})>"



alex = Person("Alex", 29, ["playing video games", "cooking", "coding"])

print(alex)
