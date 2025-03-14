#나무 사이의 최대공약수를 찾아서 배치 하면 됨

import math 
from functools import reduce

n = int(input())
list_1 = []
distances = []

for i in range(n):
  a = int(input())
  list_1.append(a)

for i in range(n-1):
  distances.append(list_1[i+1]-list_1[i])

#최대 공약수 내장함수
gcd_value = reduce(math.gcd,distances)
dist = []

for ul in distances:
  dist.append(ul/gcd_value -1)

print(int(sum(dist)))