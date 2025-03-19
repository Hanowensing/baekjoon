#기존 리스트는 시간초과가 뜸
#따라서 이진탐색을 이용함 (binary_search)
#절반부터 그 값이 큰지 작은지를 비교하며 찾는 방법
import bisect

n = int(input())
list_1 = sorted(list(map(int,input().split())))
m = int(input())
list_2 = list(map(int,input().split()))

def binary_search(arr,x):
  left,right = 0, len(arr)-1
  while left<=right:
    mid = (left+right)//2
    if arr[mid] == x:
      return True
    elif arr[mid] < x:
      left = mid+1
    elif arr[mid] >x:
      right = mid-1
  return False

for ul in list_2:
  if binary_search(list_1,ul):
    print(1)
  else:
    print(0)
