n = int(input())
list_1 = []

for i in range(n):
  b = input()
  if b in list_1:
    continue
  else:
    list_1.append(b)

#문자 길이에 따라 정렬, ord[x[0]]을 사용해 앞글자 기준 알파벳 정렬
#lambda 자세히 살펴보고 이해할 것!!!!!!!!!!!!!!!!!
list_1.sort(key=lambda x: (len(x),x.lower()))

for word in list_1:
  print(word)