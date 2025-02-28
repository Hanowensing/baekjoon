
a = int(input())


count = 0
start = 666

while True:
  #이 문법이 주요 키포인트
  if '666' in str(start):
    count += 1
  
  if count == a:
    print(str(start))
    break
    
    
  start += 1
