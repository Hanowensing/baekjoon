a = input()
discount = 0

for i in range(len(a)-1):
  if (a[i:i+2] == 'c=' or a[i:i+2] == 'c-' or a[i:i+2] == 'd-' or
        a[i:i+2] == 'lj' or a[i:i+2] == 'nj' or a[i:i+2] == 's=' or a[i:i+2] == 'z='):
    discount -= 1

for j in range(len(a)-2):
  if a[j]+a[j+1]+a[j+2] == 'dz=':
    discount -= 1

print(len(a)+discount)
