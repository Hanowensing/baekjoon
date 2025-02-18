#로직이 좀 복잡해서 40분 정도 걸렸음 

a = int(input())
list_1 = [0]*26
count = 0 

for i in range(a):
  b = input()
  for char in b:
    index = ord(char.upper())-ord('A')
    list_1[index] += 1
  for j in range(len(b)-1):
    if b[j] == b[j+1]:
      list_1[ord(b[j].upper())-ord('A')] -= 1
    elif b[j] != b[j+1]:
      continue
  if max(list_1) > 1:
    count += 0
  else:
    count += 1
  
  list_1 = [0]*26

  

print(count)

      