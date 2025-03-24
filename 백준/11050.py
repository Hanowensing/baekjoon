n,k = map(int,input().split())
n_res = 1
k_res = 1

for i in range(k):
  n_res = n_res*n
  n -= 1

  k_res = k_res*k
  k -=1

print(int(n_res/k_res))