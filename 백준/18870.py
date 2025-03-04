a = int(input())
list_1 = list(map(int,input().split()))

#sort는 기존 리스트를 변경하지만 sorted는 기존 리스트를 건드리지 않음
sorted_unique = sorted(set(list_1))

dict = {sorted_unique[i]:i for i in range(len(sorted_unique))}

for x in list_1:
  print(dict[x], end= ' ')