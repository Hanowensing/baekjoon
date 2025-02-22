#단순 반복문 쓰면 쉽긴 한데 간단하게 만들 수 있도록 노력할 것

n = int(input())

num =1
cnt = 1

while n > num:
  num += 6*cnt
  cnt += 1

print(cnt)