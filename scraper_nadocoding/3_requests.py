import requests

res = requests.get("https://www.google.com/")
# 에러가 났을때 코드를 정지시켜줌. res이후에 습관적으로 적어놓는게 좋다
res.raise_for_status() 

# print('response code:', res.status_code) # 200 OK

# if res.status_code == requests.codes.ok:
    # print('OK')
# else:
#   print('error occured:[error code ", res.status_code"]')

print(len(res.text))

# 구글을 html 파일로 만들어보기
with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)