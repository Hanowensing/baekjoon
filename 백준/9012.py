#9012
n = int(input())

for i in range(n):
  list_1 = list(input().strip())
  
  
  count_1 = 0

  for i in range(len(list_1)):
    
    if list_1[i] == '(':
      count_1 += 1
    elif list_1[i] ==')':
      count_1 -= 1

    if count_1 < 0:
      print('NO')
      break

    
  if count_1 ==0:
    print('YES')
  elif count_1 <0:
    continue
  elif count_1 >0:
    print('NO')
