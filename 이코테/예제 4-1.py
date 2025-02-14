a = int(input())
moves = list(input().split())
x,y = [1,1]

dx= [0,0,-1,1]
dy= [-1,1,0,0]
move_types = ['L','R','U','D']

for move in moves:
  for i in range(len(move_types)):
    if move == move_types[i]:
      nx = x+dx[i]
      ny = y+dy[i]
      if nx< 1 or nx> a or ny<1 or ny>a:
        continue
      
      x,y = nx,ny
  
print(x,y)
  

