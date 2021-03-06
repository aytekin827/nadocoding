import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig",newline="") # 엑셀파일로 열때 한글이 깨진다면 utf-8-sig로 설정해주면 된다
writer = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title) # writerow에서는 리스트를 변수로 받는다

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # print(data)
        writer.writerow(data)