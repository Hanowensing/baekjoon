list_9 = [[0]*9 for i in range(9)]
max_value = -1
max_row = 0
max_col = 0

for i in range(9):
    list_9[i] = list(map(int,input().split()))

for i in range(9):
  for j in range(9):
    if list_9[i][j] > max_value:
      max_value = list_9[i][j]
      max_row, max_col = i,j

print(max_value)
print(max_row+1, max_col+1)
  
  
    