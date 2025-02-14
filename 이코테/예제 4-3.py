a = str(input())
x,y = 1,1
alph = 'abcdefgh'
count = 0
steps = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,-2),(-1,2)]

for al in alph:
  if str(a[0]) == al:
    x = (alph.index(al))+1
    y = int(a[1])
  

for step in steps:
  nx,ny = x+step[0],y+step[1]
  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue
  else:
    count += 1

print(count)

##[] 리스트 형뿐만이 아니라 () 튜플형도 [] 위치 접근 가능