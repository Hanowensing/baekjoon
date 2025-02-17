a = input().lower()

alpha = 'abcdefghijklmnopqrstuvwxyz'
list_1 = [0]*26

for char in a:
  if char in alpha:
    list_1[alpha.index(char)] += 1

if list_1.count(max(list_1)) > 1:
  print("?")
else:
  index = list_1.index(max(list_1))
  print(alpha[index].upper())