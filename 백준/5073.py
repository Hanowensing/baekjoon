while True:
  a,b,c = map(int,input().split())
  if a==0 and b==0 and c==0:
    break
  
  if a==b==c:
    print('Equilateral')
  elif a==b or a==c or b==c:
    if max(a,b,c) >= (a+b+c-max(a,b,c)):
      print('Invalid')
    else:
      print('Isosceles')
  elif a!=b and b!=c and c!=a:
    if max(a,b,c) >= (a+b+c-max(a,b,c)):
      print('Invalid')
    else:
      print('Scalene')
  