class ClassTest:
  # This is an instance method since it is called
  # on an instance of the class.
  def instance_method(self):
    print(f"Called instance_method of {self}")
  

  # Class methods are called on the class itself.
  @classmethod
  def class_method(cls):
    print(f"Called class_method of {cls}")

  
  # Static methods receive no parameters.
  # It has no info about the class or an instance.
  @staticmethod
  def static_method():
    print ("Called static_method")


