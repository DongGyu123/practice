# score_file =open("score.txt", "w", encoding="utf8")
# print("수학: 0", file=score_file)
# score_file.close()

score_file=open("score.txt", "a", encoding="utf8") #기존의 파일에 내용 추가
score_file.write("\n과학: 80")
score_file.write("\n코딩: 100")
