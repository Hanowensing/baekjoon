a = int(input())

for i in range(a):
  #각 자리 숫자 더하는 기능 숙지할 것
  # 제일 작은 수를 찾는 거니까 1부터 시작해서 break, list_1 필요 X
  if i+sum(map(int,str(i))) == a:
    print(i)
    break
else:
  print(0)
