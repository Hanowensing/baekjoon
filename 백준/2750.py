a = int(input())
list_1 = []

for i in range(a):
  b = int(input())
  list_1.append(b)

for i in range(a):
  print(min(list_1))
  list_1.remove(min(list_1))
  
