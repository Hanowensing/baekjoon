list_1 = []
list_2 = []
a1 = 0
b1 = 0

for i in range(3):
  a,b = map(int,input().split())
  list_1.append(a)
  list_2.append(b)

for a_1 in list_1:
  if list_1.count(a_1) == 1:
    a1 = a_1

for b_1 in list_2:
  if list_2.count(b_1) == 1:
    b1 = b_1

print(a1,b1)
