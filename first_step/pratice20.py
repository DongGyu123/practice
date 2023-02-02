# #파일을 읽어보기
# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.read())

# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.readline())#줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline())
# score_file.close()

score_file=open("score.txt", "r", encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line)


lines=score_file.readlines() #list 형태로 저장
