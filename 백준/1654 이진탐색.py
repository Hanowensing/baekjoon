n,m = map(int,input().split())

lines = [int(input()) for _ in range(n)]
result = 0
end = max(lines)

start=1
while start<= end:
  mid = (start+end)//2
  total = sum(line//mid for line in lines)

  if total>= m:
    result = mid
    start = mid+1

  else:
    end = mid-1

print(result)
