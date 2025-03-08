#1. 최대공약수 구하기 (유클리드 호제법 사용)
#2. 구한 최대 공약수를 a*b에서 나눠주면 최대공배

t = int(input())

#최대공약수 구하는 함수
def euclide(x,y):
  while y != 0:
    x,y = y, x%y 
  return(x)

for i in range(t):
  a,b = map(int,input().split())
  print(int((a*b)/euclide(a,b)))



  