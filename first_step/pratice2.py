#문자열
"""
sentence='나는 소년입니다.'
print(sentence)
sentence2="파이썬은 쉬워요"
print(sentence2)

print(sentence3)

#슬라이싱: 문장 중에서 일부분만 잘라서 사용하는 것
jumin="990120-1234567"
print("성별: "+jumin[7])
print("연 : "+jumin[0:2])
"""
#문자열 처리 함수
python="python is amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())#대문자인지 판별하는 코드
print(len(python))
print(python.replace("python", "Java"))#문장의 특정 부분을 교체하는 코드
index=python.index("n")
print(index)
index=python.index("n", index+1)
print(index)