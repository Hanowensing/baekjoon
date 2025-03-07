a,b = map(int,input().split())

list_1 = set(list(map(int,input().split())))
list_2 = set(list(map(int,input().split())))

count_1 = len(list_1)
count_2 = len(list_2)

for li in list_1:
  if li in list_2:
    count_1 -= 1

for ul in list_2:
  if ul in list_1:
    count_2 -= 1

print(count_1+count_2)