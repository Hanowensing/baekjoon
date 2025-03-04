# 입력 받기
#a = int(input())

#count = 0
#result = []

#list_1 = list(map(int,input().split()))
#set() --> 중복값 제거
#unique_list = set(list_1)

#for li in list_1:
  #중복값 제거한 리스트로 비교
  #for ul in unique_list:
    #if li>ul:
      #count +=1
  
  #result.append(count)
  #count = 0

#print(' '.join(map(str,result)))

#-------------------------------------------------------------
#시간 초과 오류 (시간 복잡도 O(N^2))
#-------------------------------------------------------------
#list_index[i]의 시간복잡도는 O(N) 이지만
# 딕셔너리로 접근 해 dic[i]의 시간복잡도는 O[1]임

#즉 중복을 제거하고 정렬한 것을 dict로 저장하고 
#정렬 순서대로 index 부여
#기존 리스트에서 value에 맞게 index 찾기

a = int(input())
list_1 = list(map(int,input().split()))

#sort는 기존 리스트를 변경하지만 sorted는 기존 리스트를 건드리지 않음
sorted_unique = sorted(set(list_1))

dict = {sorted_unique[i]:i for i in range(len(sorted_unique))}

for x in list_1:
  print(dict[x], end= ' ')