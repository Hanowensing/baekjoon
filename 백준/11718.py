#try와 except를 사용해서 문자가 끝날때까지 반복
#d
while True:
  try:
    a = input()
    print(a)
  except EOFError:
    break