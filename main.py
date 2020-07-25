from random import *
# 3 ~28 일중에 하루 선택해서 오프라인 
# 3일 선택해서 온라인 스터디 


offlinedate = randint(3, 28)
print("오프라인 스터디는 %d일에 진행합니다."%(offlinedate))

a = randint(3, 28)

b = randint(3, 28)

c = randint(3, 28)

#중복제거 
while a == offlinedate :
  a = randint(3, 28)

while b == offlinedate :
  b = randint(3, 28)
  if( b == a ):
    b = randint(3, 28)
  

while c == offlinedate :
  c = randint(3, 28)
  if( c == a ):
    c = randint(3, 28)
    if( c == b ):
      c = randint(3, 28)
  

print("온라인 스터디는 %d, %d, %d일에 진행합니다."%(a,b,c))

