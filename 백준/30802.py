n = int(input())
list_1 = list(map(int,input().split()))
t,p = map(int, input().split())

count = 0
for i in range(len(list_1)):
  if list_1[i]%t ==0:
    count += list_1[i]/t
  elif list_1[i]%t !=0:
    count += (list_1[i]//t)+1

print(int(count))
  
a= n//p
b= n%p

print(' '.join(map(str,(a,b))))
