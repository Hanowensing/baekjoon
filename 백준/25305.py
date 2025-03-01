a,b = map(int,input().split())
list_1 = list(map(int,input().split()))

for i in range(a-b):
  list_1.remove(min(list_1))


print(min(list_1))