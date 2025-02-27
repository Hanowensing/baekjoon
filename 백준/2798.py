a,b = map(int,input().split())
result = 0
list_1 = []
list_input = list(map(int,input().split()))

for i in range(a-2):
  for j in range(i+1,a-1):
    for k in range(j+1,a):
      result = list_input[i]+list_input[j]+list_input[k]
      if (b-result) >= 0:
        list_1.append(b-result)
    

print(b-min(list_1))

