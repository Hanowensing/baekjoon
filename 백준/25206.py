total_sco = 0
total_les = 0
for i in range(20):
  a,b,c = input().split()  
  b = float(b)
  sco = 0 
  if c == 'P':
    continue
  if c == 'A+':
    sco = 4.5
  elif c == 'A0':
    sco =  4.0
  elif c == 'B+':
    sco = 3.5
  elif c == 'B0':
    sco = 3.0
  elif c == 'C+':
    sco = 2.5
  elif c == 'C0':
    sco = 2.0
  elif c == 'D+':
    sco = 1.5
  elif c =='D0':
    sco = 1.0
  else:
    sco = 0.0

  total_sco += (sco*b)
  total_les += (b)

result = total_sco / total_les
print(result)    
