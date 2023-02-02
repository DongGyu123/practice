#IF
weather=input("오늘 날씨는 어때요?") #input: 사용자가 값을 직접 입력 

if weather=="비":
    print("우산을 챙기세요")
elif weather=="미세먼지":
    print("마스크를 챙기세요")

else: 
    print("준비 안해도 되요")


tem=int(input("기온은 어때요?"))

if 3<=tem:
    print("너무 더워요 나가지 마세요.")
elif 10<= tem and tem<30:
    print("날씨가 적당해요~")
