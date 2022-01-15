# class Book is meant to demonstrate the use of class methods.

class Book:
  # TYPES is a class property.
  # Book.TYPES will expose this tuple.
  TYPES = ("hardcover", "paperback", "ebook", "audiobook")

  def __init__(self, name, book_type, weight=0):
    self.name = name
    self.book_type = book_type
    self.weight = weight


  def __repr__(self):
    return f"<Book Object name: '{self.name}' book_type: '{self.book_type}' weight: {self.weight}g>"

    
  @classmethod
  def add_hardcover(cls, name, page_weight):
    return cls(name, Book.TYPES[0], page_weight + 100)


  @classmethod
  def add_paperback(cls, name, page_weight):
    return cls(name, Book.TYPES[1], page_weight)

  
  @classmethod
  def add_ebook(cls, name):
    return cls(name, Book.TYPES[2])

  
  @classmethod
  def add_audiobook(cls, name, page_weight):
    return cls(name, Book.TYPES[3])

  
book = Book.add_hardcover("Harry Potter", 1500)
book2 = Book.add_paperback("Python 101", 1100)
print(book)
print(book2)
