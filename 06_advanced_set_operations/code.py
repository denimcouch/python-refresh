friends = {"Alex", "Karo", "Zack", "Lauren"}
abroad = {"Alex", "Karo"}

local_friends = friends.difference(abroad)

print(local_friends)

local = {"Brian", "Kaylee"}

union = local.union(abroad)

print(union)