#집합(set)
#중복되지 않음. 순서가 없음
my_set={1, 2, 3, 3, 2}
print(my_set)
java={"a", "b","c","d"}
python={"a", "a", "f", "z"}
print(python)
#교집합
print(java&python)#(java.intersection(python)) 도 같은 기능임
#합집합
print(java|python)#(java.union(python))도 같은 기능을 함
#차집합(java는 가능 python는 불가능)
print(java-python)#(java.difference(python))도 같은 기능을 함
#집합에 값을 추가/삭제
java.add("안녕하세요")
java.remove("a")
print(java)