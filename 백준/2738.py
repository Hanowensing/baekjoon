a,b = map(int,input().split())

# b 문자 갯수가 a 번 반복될 때 사용하는 문법
mat_1 = [list(map(int,input().split())) for _ in range(a)]
mat_2 =[list(map(int,input().split())) for _ in range(a)]
mat_3 = [[0]*b for i in range(a)]

for i in range(a):
  for j in range(b):
    #2차원 행렬 row,column 접근할 시 다음과 같은 문법을 사용해야함
    mat_3[i][j] = mat_1[i][j]+mat_2[i][j]

#list로 받은 인자들을 숫자로 바꿔서 내보내기
for row in mat_3:
  print(" ".join(map(str,row)))
