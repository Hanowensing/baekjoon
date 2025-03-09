a,b = map(int,input().split())
c,d = map(int,input().split())

def euclid(x,y):
  while y!= 0:
    x,y = y,x%y
  return x


#기약분수로 바꾸기
def simplify(x,y):
  gcd =euclid(x,y)
  return x//gcd ,y//gcd

#여기 정수형 쓰면 안됨, 소수점이 날라가버리니까
#대신에 //를 써야
mother = (b*d) // euclid(b,d)
son = (a*(mother//b)) + (c*(mother//d))


son,mother = simplify(son,mother)

print(son,mother)

