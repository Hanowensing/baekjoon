s = input()

cnt = set()

#중복 리스트 잘 이해하기
for i in range(len(s)):
  for j in range(i,len(s)):
    #set에서는 add로 추가 list에서는 append
    cnt.add(s[i:j+1])

print(len(cnt))