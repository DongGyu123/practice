#지역변수와 전역변수
'''
gun=10

def checkpoint(soldiers):#경계근무
    gun=20
    gun=gun-soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
print("전체 총: {0}".format(gun))
checkpoint(2)
print("남은 총: {0}".format(gun))
'''

gun=10

def checkpoint(soldiers):#경계근무
    global gun #전역변수
    gun=gun-soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_return(gun, soldier):
    gun=gun-soldier
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
#checkpoint(2) #아래와 비교
gun=checkpoint_return(gun, 2)
print("남은 총: {0}".format(gun))
