"""#absent =[2, 5] #결석
no_book=[7] #책을 깜빡했음
for student in range (1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0}번 너 교무실로 와라".format(student))
        break
    print("{0}번 책 읽어라".format(student))

#출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함->101, 102, 103, 104.
student=[1, 2,3, 4, 5]
student=[i+100 for i in student]
print(student)
"""

#퀴즈 내가 코코아 서비스를 이용하는 택시 기사일 때, 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 짜라
#조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해짐
#조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 한다.
from random import *
a=0
for cus2 in range(1, 50):
    time=randrange(5, 50)
    if time>=5 and time<=15:
        print("[O] {0}번째 손님 (소요시간: {1}분)".format(cus2, time))
        a+=1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(cus2, time))
    
print("총 탑승 승객: {0}분".format(a))

