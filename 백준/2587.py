list_1 = []

for i in range(5):
  a = int(input())
  list_1.append(a)

print(int(sum(list_1)/5))
for i in range(2):
  list_1.remove(max(list_1))

print(max(list_1))
