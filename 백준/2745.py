n,b = input().split()
b= int(b)
result = 0

for i in range(len(n)):

  #진법은 뒤에서부터 계산해야함
  char = n[len(n)-i-1]

  #'A1B'에서 숫자가 어딨는지 찾아내는 것 (문자열 안에서)
  if char.isdigit():
      result += int(char)*(b**i)
  else:
    index = ord(char)-ord('A')
    result += (index+10)*(b**i)

print(result)
