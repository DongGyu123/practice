#함수 기본값
'''
def profile(name, age, main_lang):
    print("이름: {0}\n나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")

def profile2(name, age=17, main_lang="c언어"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))
profile2("임동규")
'''

"""
#키워드값
def profile3(name, age, main_lang):
    print(name, age, main_lang)
profile3(name="유잭석", main_lang="파이썬", age=20)
profile3(age=1,name="임동규", main_lang="자바")
"""
'''
def pro(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")#end=""를 사용하면 줄바꿈이 일어나지 않음
    print(lang1, lang2, lang3, lang4, lang5)

pro("이한성", 20, "python", "java", "c", "c++", "c#")'''

#가변인자

def pro2(name, age, *lang1):
    print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ")
    for lang in lang1:
        print(lang, end=" ")
    print()    

pro2("유재석", 20, "파이썬", "자바", "c언어")
pro2("박재현", 17, "스프링")
