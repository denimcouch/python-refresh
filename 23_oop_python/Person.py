class Person:
  def __init__(self, name, age, hobbies=[]):
    self.name = name
    self.age = age
    self.hobbies = hobbies


  def __str__(self):
    return f"Person {self.name}, {self.age} years old."

  
  def __repr__(self):
    return f"<Person Object('{self.name}', {self.age}, {self.hobbies})>"



alex = Person("Alex", 29, ["playing video games", "cooking", "coding"])

print(alex)