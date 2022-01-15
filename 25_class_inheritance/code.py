# Inheritance allows classes to take certain properties from other classes.

class Device:
  def __init__(self, name, connected_by):
    self.name = name
    self.connected_by = connected_by
    self.connected = True


  def __repr__(self):
    return f"<DeviceObject name:{self.name!r} connected_by:{self.connected_by!r} connected:{self.connected!r}>"


  def connect(self):
    self.connected = True
    print("Device connected successfully!")

  
  def disconnect(self):
    self.connected = False
    print("Device disconnected.")


class Printer(Device):
  def __init__(self, name, connected_by, capacity):
    super().__init__(name, connected_by)
    self.capacity = capacity
    self.remaining_pages = capacity

  
  def __repr__(self):
    return f"{super().__repr__()} ({self.remaining_pages} pages remaining)"


  def print_something(self, pages):
    if not self.connected:
      print("Your printer is not connected:")
      return
    print(f"Printing {pages} pages")
    self.remaining_pages -= pages

