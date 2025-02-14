a,b = map(str,input().split())

a,b = a[::-1],b[::-1]
#문자열 거꾸로 출력 [::-1] 기억하기

print(max(a,b))
