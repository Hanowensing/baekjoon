a1, a0 = map(int,input().split())
c= int(input())
n0 = int(input())

def f(a1,a0,n0):
  return(a1*n0+a0)

result = f(a1,a0,n0)


if f(a1,a0,n0) <= c*n0 and a1<=c:
  print(1)
else:
  print(0)
