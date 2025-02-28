n = int(input())
list_1 = []
count = 0


for i in range(n//3):
  count = n-(3*i)
  if count % 5 == 0:
    list_1.append(int(i+(count/5)))
  elif count % 3 ==0:
    list_1.append(int(n/3))

if len(list_1) == 0:
  print(-1)
else:
  print(min(list_1))

