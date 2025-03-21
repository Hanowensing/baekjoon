import sys  # 입력 속도 개선
from collections import deque

n = int(sys.stdin.readline().strip())
list_1= deque() #입력 속도 개선

for i in range(n):
  a = sys.stdin.readline().strip().split()
  if a[0] == 'push':
    list_1.append(a[1])
  elif a[0] == 'pop':
    if len(list_1) == 0:
      print(-1)
    else:
      print(list_1[-1])
      #리스트 마지막 값 삭제에는 pop이 더 적절
      list_1.pop()
  elif a[0] == 'size':
    print(len(list_1))
  elif a[0] == 'empty':
    if len(list_1) == 0:
      print(1)
    else: 
      print(0)
  elif a[0] == 'top':
    if len(list_1) ==0:
      print(-1)
    else:
      print(list_1[-1])