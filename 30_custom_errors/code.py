class Book:

  def __init__(self, name: str, page_count: int):
    self.name = name
    self.page_count = page_count
    self.pages_read = 0


  def __repr__(self):
    return f"<BookObject name:{self.name!r} page_count:{self.page_count!r} pages_read:{self.pages_read!r}>" 


  def read(self, pages: int):
    if self.pages_read + pages > self.page_count:
      raise TooManyPagesReadError(
        f"You have tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
      )
    self.pages_read += pages
    print(f"You have read {self.pages_read} pages out of {self.page_count}")


class TooManyPagesReadError(ValueError):
  pass
