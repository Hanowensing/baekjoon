n = int(input())

line = 0
end = 0

while n> end:
  line += 1
  end += line

bottom =0
top = 0

if line %2 != 0:
  top = 1+ (end-n)
  bottom = (line+1)-top
  print(str(top)+'/'+str(bottom))
else:
  top = 1+ (end-n)
  bottom = (line+1)-top
  print(str(bottom)+'/'+str(top))

