a,b = map(int,input().split())
list_1=[]
result = 0

for i in range(1,a+1):
  if a%i ==0:
    list_1.append(i)

if len(list_1) < b:
  print(0) 
else:
  result = print(list_1[b-1])
