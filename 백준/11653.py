a = int(input())

for i in range(2,a+1):

  if a ==1:
    print()
    break
  while a%i ==0:
    print(i)
    a = a/i