a = int(input())
dict = {}

for i in range(a):
  a,b = input().split()
  #딕셔너리 key(a), value(b) 추가법
  dict[a] = b
  
  if dict[a] == 'leave':
    #딕셔너리에서 값 삭제 함수 pop()
    del dict[a]

#딕셔너리 역순 배열
dict_result = sorted(dict.keys(),reverse=True)

for dic in dict_result:
  print(dic)