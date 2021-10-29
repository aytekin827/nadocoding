# import requests
# from bs4 import BeautifulSoup

# url = 'https://play.google.com/store/movies?hl=ko&gl=US'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.232 Whale/2.10.124.26 Safari/537.36",
# "Accept-Language":"ko-KR,ko"}

# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, 'lxml')

# movies = soup.find_all("div",attrs={"class":"WHE7ib mpg5gc"})
# print(len(movies))

# # with open ("movie.html","w",encoding='utf-8') as f:
#     # f.write(res.text)
#     # f.write(soup.prettify())# 문서를 예쁘게 출력

# for movie in movies:
#     title = movie.find("div",attrs={"class":"b8cIId ReQCgd Q9MA7b"}).get_text()
#     print(title)

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies?hl=ko&gl=US"
browser.get(url)

# 스크롤 내리기
# 모니터의 (해상도) shvdldls 1080위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,2080)")

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    # prev_height값 업데이트하기
    prev_height = curr_height

print("\n====== scroll completed! =====\n")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source,'lxml')

movies = soup.find_all("div",attrs={"class":"WHE7ib mpg5gc"})
# movies = soup.find_all("div",attrs={"class":["WHE7ib mpg5gc"]})
# 클래스명을 리스트[]로 감싸주면 OR연산자 기능을 하도록 할 수 있다.
print('total number of movies: ',len(movies))

for movie in movies:
    title = movie.find("div",attrs={"class":"b8cIId ReQCgd Q9MA7b"}).get_text()

    # 할인이 진행중인 영화만 스크롤링하기
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, '==== 할인되지 않은 영화는 제외 ===')
        continue

    # 할인된 가격
    price = movie.find("span",attrs={'class':'VfPpfd ZdBevf i5DZme'}).get_text()

    # 링크
    link = movie.find("a",attrs={'class':'JC71ub'})['href']
    # 올바른 링크 : https://play.google.com/ + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f'할인 후 금액 : {price}')
    print("링크 : ","https://play.google.com" + link)
    print("*" * 100)