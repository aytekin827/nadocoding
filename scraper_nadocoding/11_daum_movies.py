import requests
from bs4 import BeautifulSoup
import os 


path = os.getcwd()
for year in range(2015,2020):
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,'lxml')

    images = soup.find_all("img",attrs={"class":"thumb_img"})

    for index, image in enumerate(images):
        # print(image['src'])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # movie라는 폴더에 이미지파일 저장하기
        with open(path+"\movie\{} movie{}.jpg".format(year,index+1), "wb") as f:
            f.write(image_res.content)
            # 상위 5개의 이미지까지만 다운로드 하겠음

        if index == 4:
            break