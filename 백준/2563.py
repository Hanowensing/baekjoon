#전체 도화지를 0으로 두고 입력값 범위마다 1 추가
#차피 1추가한 곳에 또 1 추가해봤자 중복 값 반영되지 않암1
a = int(input())
blank = [[0]*100 for _ in range(100)]

for i in range(a):
  l,d = map(int,input().split())
  for j in range(10):
    for k in range(10):
      blank[d+j][l+k] = 1

#blank에 count 사용 불가
#blank는 여러 리스트로 이루어져있으므로 [0,1,1]과 같은 리스트만 찾을 수 있음
#따라서 row.count(1) 우선 한 로우에서 1을 카운트하고
#blank 안 row 개수만큼 반복해서 찾아내는 수 밖에 없음
print(sum(row.count(1) for row in blank))



#2차원 배열 많이 약한듯