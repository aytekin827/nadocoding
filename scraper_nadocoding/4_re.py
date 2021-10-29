# 정규식
import re

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미한다. > care, cake, case, (0) | acffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (0) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (0) | face(X)

# print(m.group()) # 매칭되지 않으면 에러 발생
def print_match(m):
    if m:
        print("m.group():",m.group()) # 일치하는 문자열 반환
        print("m.string:",m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index 표시
    else:
        print('not matched')

m = p.match("goodcareof") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)

print()

m = p.search("goodcareof") # search : 주어진 문자열 중에 일치하는게 있는지
print_match(m)

lst = p.findall("careless") # findall : 일치하는 모든 것을 리스트 형태로 변환
print(lst)

lst = p.findall("careless care cafe") # findall : 일치하는 모든 것을 리스트 형태로 변환
print(lst)

# 1. p = re.compile("원하는 정규식 형태")
# 2. m=p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m=p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. m=p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미한다. > care, cake, case, (0) | acffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (0) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (0) | face(X)