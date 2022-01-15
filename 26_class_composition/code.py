# Class composition is more widely used in Python instead of inheritance.
# Composition is useful for defining relationships between objects.

class BookShelf:
  def __init__(self, *books):
    self.books = [book for book in books]

  
  def __str__(self):
    return f"BookShelf with {len(self.books)} books."

  
  def add_books(self, *books):
    for book in books:
      self.books.append(book)


class Book:

  def __init__(self, name, page_count):
    self.name = name
    self.page_count = page_count

  
  def __str__(self):
    return f"Book {self.name}"


  def __repr__(self):
    return f"<BookObject name:{self.name!r} page_count:{self.page_count!r}>" 


b1 = Book("Harry Potter", 500)
b2 = Book("Python 101", 225)
b3 = Book("Monster Manual", 600)

bs1 = BookShelf(b1, b2)
print(bs1.books)

bs1.add_books(b3)
print(bs1.books)
