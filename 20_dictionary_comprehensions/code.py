users = [
  (0, "Alex", "password"),
  (1, "Karo", "password1"),
  (2, "Zack", "password2"),
  (3, "Lauren", "password3"),
]

# Dictionary Comprehensions work similar to List Comprehension
# In the example below, the username_mapping variable's value will be
# a dictionary where each key is the user's name with the entire user tuple as the value
#  => {
#       'Alex': (0, 'Alex', 'password'), 
#       'Karo': (1, 'Karo', 'password1'), 
#       'Zack': (2, 'Zack', 'password2'), 
#       'Lauren': (3, 'Lauren', 'password3')
#     }
username_mapping = {user[1]: user for user in users}
print(username_mapping)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password == password_input:
  print(f"Welcome {username}!")
else:
  print("username or password is incorrect.")