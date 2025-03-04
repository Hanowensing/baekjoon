a = int(input())
list_1 = []

for i in range(a):
  b,c = input().split()
  b = int(b)
  list_1.append([b,c])

list_1.sort(key= lambda x:x[0])

for li in list_1:
  print(' '.join(map(str,li)))
  
