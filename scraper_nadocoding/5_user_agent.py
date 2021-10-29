import requests
url = "https://aytekin.tistory.com/"
# user agent 를 써야하는 상황이 있을 수 있다. 
# 정확하게 용도는 이해하지 못함..
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.232 Whale/2.10.124.26 Safari/537.36"}
res = requests.get(url)
res.raise_for_status() 
with open("티스토리.html", "w", encoding="utf-8") as f:
    f.write(res.text)