n,m = map(int,input().split())
list_1 = []
list_2 = []
count = 0
dict1= {}

for i in range(n):
  listen = input()
  dict1[listen] = i

for j in range(m):
  see = input()
  if see in dict1:
    count += 1
    list_2.append(see)

list_2.sort()

print(count)
for x in list_2:
  print(x)
