a = int(input())
list_1 = []

for i in range(a):
  b,c = list(map(int,input().split()))
  list_1.append([b,c])

# *** 람다 사용해서 sort 우선 순위를 y좌표로 변신
list_1.sort(key = lambda x: (x[1], x[0]))

for i in range(a):
  print(' '.join(map(str,list_1[i])))



  

