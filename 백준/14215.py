max_1 = 0
a,b,c = map(int,input().split())

if max(a,b,c) >= a+b+c-max(a,b,c):
  max_1 = a+b+c-max(a,b,c)-1
  print(max_1+(a+b+c-max(a,b,c)))
else:
  print(a+b+c)
