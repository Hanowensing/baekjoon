a = int(input())
x_1 = []

for i in range(a):
  [b,c]= list(map(int,input().split()))

  x_1.append([b,c])
  
x_1.sort()

for i in range(a):
  print(' '.join(map(str,x_1[i])))
  
   
