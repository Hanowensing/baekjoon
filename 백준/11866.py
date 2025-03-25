m,n = map(int,input().split())

lst = list(range(1,m+1))
result = []
count = 0

while lst:

  count = (count+n-1)%len(lst)
  result.append (lst.pop(count))

print(f"<{', '.join(map(str, result))}>")