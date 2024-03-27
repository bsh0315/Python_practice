dic_test = {"name" : "bfdfh"}
dic_test["birth"] = 20030315
dic_test["birth"] = 11997546
print(dic_test)
# 기본형 : 딕셔너리명 =  {"key" : Value, ...}
# 추가하는 법 : 딕셔너리명[key(존재하지 않는것)] = ~
# 삭제하는법 : del 딕셔너리명[key]
# 값을 가져오는법 : 딕셔너리명[key]
# 딕셔너리명[key] vs 딕셔너리명.get(key)의 차이
#딕셔너리명.get(key)는 존재하지않은 key를 불러내어도 오류가 나지않고 False값을 봔환함.