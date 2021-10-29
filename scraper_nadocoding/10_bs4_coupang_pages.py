import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.232 Whale/2.10.124.26 Safari/537.36"}

for i in range(1,6):
    # print("<{}페이지 입니다>".format(i))
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)

    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div",attrs={"class":"name"}).get_text())
    for item in items:

        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("  <광고 제품은 제외합니다>  ")
            continue
        name = item.find("div",attrs={"class":"name"}).get_text() # 제품 명

        # HP 제품 제외
        if "Apple" in name:
            # print("  < Apple 제품 제외합니다 >  ")
            continue

        price = item.find("strong",attrs={"class":"price-value"}).get_text()

        # 리뷰 100개 이상 , 평점 4.5 이상 되는 것만 조회하는
        rating = item.find("em",attrs={"class":"rating"})
        if rating:
            rating = rating.get_text()
        else:
            rating = "평점 없음"
            # print(" < 평점 없는 제품은 제외합니다> ")
            continue

        num_rating = item.find("span",attrs={"class":"rating-total-count"})
        if num_rating:
            num_rating = num_rating.get_text()
            num_rating = num_rating[1:-1]
        else:
            num_rating = "평점 수 없음"
            # print(" < 평점 없는 제품은 제외합니다> ")
            continue
        link = item.find("a",attrs={"class":"search-product-link"})['href']

        if float(rating) >= 4.5 and int(num_rating) >= 1100:
            # print(name,price,rating,num_rating)
            print(f'name : {name}')
            print(f'price : {price}')
            print(f'rating : {rating} cnt_rate : {num_rating}')
            print('link : {}'.format("https://www.coupang.com" + link))
            print('-'*100) # 줄긋기



