# Magic Number app
magic_num = 7

while True:
  user_input = input("Magic Number Guesser. Would you like to play? [Y/n] ")

  if user_input == 'n':
    print("Goodbye!")
    break

  user_num = int(input("Choose a number: "))
  if user_num == magic_num:
    print("That's correct!")
    break
  elif abs(magic_num - user_num) == 1:
    print("You were so close! Only off by 1.")
  else:
    print("Sorry, that's wrong.")
  
