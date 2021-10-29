import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies?hl=ko&gl=US'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.232 Whale/2.10.124.26 Safari/537.36",
"Accept-Language":"ko-KR,ko"}

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all("div",attrs={"class":"WHE7ib mpg5gc"})
print(len(movies))

# with open ("movie.html","w",encoding='utf-8') as f:
    # f.write(res.text)
    # f.write(soup.prettify())# 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div",attrs={"class":"b8cIId ReQCgd Q9MA7b"}).get_text()
    print(title)