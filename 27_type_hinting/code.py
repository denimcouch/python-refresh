from typing import List

# type hinting is a way to create loud errors
def average(sequence: List) -> float:
  return sum(sequence) / len(sequence)


average(123)
