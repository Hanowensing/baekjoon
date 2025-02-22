#11005번 (진법 익숙해져야함 틀림)

n,b = map(int,input().split())
count = []
mok = 0
nam = 0

while True:
  mok = n//b
  nam = n%b

  n=mok

  if nam >= 10:
    #ord['A']로 쓰지만 chr[65]로 접근 가능 chr[65] = A, chr[90] = Z
    nam = chr(nam+55)
  
  count.append(nam)

  if mok == 0:
    break

#진법에서는 출력값이 역순이 되어야 함
print(''.join(map(str,count[::-1])))


