n = int(input())
#중복 제거해도 되는 리스트에 set을 씌워줌으로써 시간복잡도 해결
list_n = set(list(map(int,input().split())))
m = int(input())
list_m = list(map(int,input().split()))

result = []

for lm in list_m:
  if lm in list_n:
    result.append(1)
  else:
    result.append(0)
 
print(' '.join(map(str,result)))

  