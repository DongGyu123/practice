#사전 개념

cabinet={3: "유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[4]) #어떻게 나오는지 확인해보자
#print(cabinet.get(5))
print(cabinet.get(3, "안녕하세요"))
print(cabinet.get(5, "안녕하세요"))
print(5 in cabinet)
print(3 in cabinet)

#사전에 새로운 값을 넣기
cabinet["A-3"]='김종국'
print(cabinet)
#사전에 기존의 값을 빼기
del cabinet[100]
print(cabinet)
#keys 들만 출력
print(cabinet.keys())
#value 들만 출력
print(cabinet.values())
#keys 와 values를 모두 출력
print(cabinet.items())
