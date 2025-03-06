n,m = map(int,input().split())
list_1 = []
count = 0

for i in range(n):
  a = input()
  list_1.append(a)

for j in range(m):
  b = input()
  if b in list_1:
    count += 1
    

print(count)