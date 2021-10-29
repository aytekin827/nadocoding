from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://realty.daum.net/home/apt/danjis/20450'

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.232 Whale/2.10.124.26 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.get(url)

browser.find_element_by_xpath("//*[@id='__next']/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/input").send_keys("동탄센트럴포레스트")
elem = browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/button')
elem.click()

import csv
filename = "최근 25개 거래정보.csv"
f = open(filename,"w",encoding='utf-8-sig',newline='')
writer = csv.writer(f)

# header 쓰기
title = "계약일 전세/월세 거래가격 타입 층수".split(" ")
writer.writerow(title)

# 최근 25개 거래정보 조회
for i in range(4):
    browser.find_element_by_xpath("//*[@id='__next']/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[1]/div[2]/div/div[4]/div/div[2]/div[3]/div/div[1]").click()

soup = BeautifulSoup(browser.page_source, 'lxml')
sold_apt_table = soup.find_all("div",attrs={"class":"css-1dbjc4n r-14lw9ot r-13awgt0 r-1mlwlqe r-eqz5dr"})[1]
sold_apt_rows = sold_apt_table.find_all("div",attrs={"class":"css-1dbjc4n r-13awgt0 r-1mlwlqe r-eqz5dr"})

for index,row in enumerate(sold_apt_rows):
    contract = row.find_all("div",attrs={"class":"css-1563yu1"})
    contract_date = contract[0].get_text()
    contract_type = contract[1].get_text()
    contract_price = contract[2].get_text()
    type_ = contract[3].get_text()
    floor = contract[4].get_text()
    print(f'===== 실거래가 {index+1} ====')
    print(f'계약일 : {contract_date}')
    print(f'거래 : {contract_type}')
    print(f'거래가격 : {contract_price} 만원')
    print(f'타입 : {type_}')
    print(f'층수 : {floor}층')
    print()
    
    contract = contract[:-1]
    data = [column.get_text() for column in contract]
    writer.writerow(data)
