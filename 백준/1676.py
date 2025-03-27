n = int(input())

result = 1
for i in range(1,n+1):
  result = result*i
  
result = str(result)

count = 0

for i in range(1,len(result)+1):
  if result[-i] == '0':
    count += 1
  else:
    break

print(count)