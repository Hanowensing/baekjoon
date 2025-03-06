import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1,n+1):
  a = input().rstrip()
  dict[a] = i
  dict[i] = a

for i in range(m):
  ques = input().rstrip()
  #숫자인지 문자인지 구분하는 함수 isdigit()
  if ques.isdigit():
    print(dict[int(ques)])
  else:
    print(dict[ques])