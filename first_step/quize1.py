#표준 체중: 각 개인의 키에 적당한 체중
"""
(성별에 따른 공식)
남자: 키(m)x키(m)x22
여자: 키(m)x키(m)x21

조건1 : 표준 체중은 별도의 함수 내에서 계산
ex)
*함수명: std_weight
*전달값: 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

"""

def std_weight(height, gender): 
    if gender == "남자":
        weight=height*height*22
    elif gender=="여자":
        weight=height*height*21
    print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, weight))

std_weight(1.65, "남자")