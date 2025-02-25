list_1 = []
list_2 = []

n = int(input())

for i in range(n):
  a,b = map(int,input().split())
  list_1.append(a)
  list_2.append(b)

print(((max(list_1)-min(list_1))*(max(list_2)-min(list_2))))

  