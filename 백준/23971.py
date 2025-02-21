h,w,n,m = map(int,input().split())

w_w = 0
h_h = 0

if w%(m+1) == 0:
  w_w = w/(m+1)
elif w%(m+1) != 0:
  w_w = (w//(m+1))+1

if h%(n+1) == 0:
  h_h = h/(n+1)
elif h%(n+1) != 0:
  h_h = (h//(n+1))+1

print(int(w_w * h_h))
