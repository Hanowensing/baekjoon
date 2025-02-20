#split() 는 ['abcde'] 이렇게 저장하지만 strip() 는 ['a','b','c'] 이렇 게저장함
matrix = [list(input().strip()) for _ in range(5)]

for i in range(15):
  for j in range(5):
    #len(matrix)는 행의 갯수를 반환함, len(matrix[i]) 는 i번재 행의 길이임
    if i < len(matrix[j]):
      print(matrix[j][i], end='')              