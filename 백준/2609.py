#2609
n,m = map(int,input().split())

#유클리드 함수 꼭꼭 기억잘하기
def euclid(x,y):
  while y!=0:
    x,y = y,x%y
  return x

print(euclid(n,m))
a = (n/euclid(n,m))*(m/euclid(n,m))
print(int(a*euclid(n,m)))