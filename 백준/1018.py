a,b = map(int,input().split())
#체스 판 입력 받기
board = [input() for _ in range(a)]

cnt = []

for i in range(a-7):
  for j in range(b-7):
    w_start = 0 #하얀색으로 시작
    b_start = 0 #검은색으로 시작

    for x in range(8):
      for y in range(8):

        if (x+y)%2 ==0: #짝수인 경우 
          if board[i+x][j+y] != 'W':
            w_start += 1
          else:
            b_start += 1
        else: #홀수인 경우
          if board[i+x][j+y] != 'B':
            w_start += 1
          else:
            b_start += 1
      
    cnt.append(w_start)
    cnt.append(b_start)
  
print(min(cnt))
       


            



