#<탈출문자>
#\n : 줄바꿈
print("qoransdl qnxdudlfrus \n백견이 붙여일타")
print('저는"나도코딩" 입니다' )
print("저는 \"나도코딩\"입니다.")

#\\: 문장 내에서 \을 출력함.
#\r : 커서를 맨 앞으로 이동
#\b : 백스페이스 (한 글자 삭제)
#\t : 탭 기능

#퀴즈: 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
#규칙1: http:// 부분은 제외
#규칙2: 처음 만나는 점 이후 부분은 제외
#규칙3: 남은 글자 중 처음 세자리+글자 갯수+글자 내 'e'개수+"!" 로 구성
url="http://google.com"
my_str=url.replace("http://", "")
my_str=my_str[:my_str.index(".")]
passward=my_str[0:2]+str(len(my_str))+str(my_str.count("e"))+"!"
print(passward)




