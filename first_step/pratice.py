#당신은 코딩 스터디 모임을 하는데 월 4회를 스터디를 함. 3번은 온라인, 1번은 만나서 함
#조건1: 랜덤으로 날짜 뽑기
#조건2: 28일 이내로 뽑기
#조건3: 매월 1~3일은 스터디 준비기간이여서 제외시킴

from random import *

time=int(random()*24)+4
print("오프라인 스터디 모임 날짜는 매월"+str(time)+"일로 선정되었습니다.")
time=int(random()*24)+4
print("온라인 스터디 모임 날짜는 매월"+str(time)+"일로 선정되었습니다.")
time=int(random()*24)+4
print("온라인 스터디 모임 날짜는 매월"+str(time)+"일로 선정되었습니다.")
time=int(random()*24)+4
print("온라인 스터디 모임 날짜는 매월"+str(time)+"일로 선정되었습니다.")
print(randrange(2, 100))
