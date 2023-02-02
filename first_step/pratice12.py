#for

#for waiting_no in [0, 1, 2, 3, 4]:
#    print("대기번호: ",format(waiting_no))

for i in range(5):
    print("대기번호: {0}".format(i))

starbucks=["아이언맨", "토르", "캡틴"]

for c in starbucks:
    print("{0}, 커피가 준비됨".format(c))

#while

customer=["토르"]
index=5
while index >=1:
    print("{0}, 커피가 준비되어습니다. {1}번 남았어요".format(customer, index))
    index-=1
    if index==0:
        print("커피가 없습니다.")
