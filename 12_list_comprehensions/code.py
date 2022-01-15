friends = ["Alex", "Karo", "Zack", "Lauren", "Brian", "Kaylee"]
nums = [1, 2, 3, 5, 7, 9]

# This is list comprehension
nums_doubled = [num ** 2 for num in nums]
print(nums_doubled)

# Adding a conditional to list comprehension
starts_k = [friend for friend in friends if friend.startswith('K')]
# for friend in friends:
#   if friend.startswith('K'):
#     starts_k.append(friend)

print(starts_k)