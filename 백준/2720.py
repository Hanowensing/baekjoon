#쉬운데 바보짓함
a = int(input())
quarter = 0 
daim = 0
nikel = 0
peni = 0
nam = 0

for i in range(a):
  c = int(input())

  quarter = c//25
  c %= 25

  daim = c//10
  c %= 10

  nikel = c//5
  peni = c % 5


  print(quarter,daim,nikel,peni)
