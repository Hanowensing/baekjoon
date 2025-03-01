#시간 초과 줄이기 위해 sys.stdin.readline() 사용하기
import sys

a = int(input())
list_1 = []

for i in range(a):
  list_1.append(int(sys.stdin.readline()))

list_1.sort()
for num in list_1:
  print(num)