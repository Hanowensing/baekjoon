#시간복잡도 유의할 것
m = int(input())
n = int(input())

yak_1 = []
for num in range(m,n+1):
  count = 0
  if num > 1:
    for j in range(2, num):
      if num%j == 0:
        count += 1
        break
    if count ==0:
      yak_1.append(num)



if len(yak_1) == 0:
  print(-1)
else:
  print(sum(yak_1))
  print(min(yak_1))
