a,b,v = map(int,input().split())

if a <= v:
  day = (v-a)//(a-b)
  if (v-a)%(a-b) != 0:
    day += 1
  print(day+1)  
else:
   print(1)


