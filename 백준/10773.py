k = int(input())

list_1 = []

for i in range(k):
  a = int(input())
  if a ==0:
    #최근 값을 지우는 방법 --> pop()
    #list_remove(list_1[-1]의 값인 3을 지움)
    #remove는 중복된 값이 있으면 앞에서부터 지움 --> 개 같네 시발
    list_1.pop()
  else:
    list_1.append(a)

print(sum(list_1))