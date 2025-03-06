a = list(map(int,input().strip()))
a.sort(reverse=True)
print(''.join(map(str,a)))