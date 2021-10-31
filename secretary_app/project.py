# 나만의 비서 만들기 - 날씨, 헤드라인 뉴스, 영어회화
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup
    
# 오늘의 날씨 출력
def scrape_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    print("[오늘의 날씨]")
    
    # 온도
    temperature = soup.find("div",attrs={"class":"temperature_text"}).get_text().strip()
    print(temperature)

    # 맑음
    weather_degree = soup.find("p",attrs={"class":"summary"}).find("span",attrs={'class':'temperature down'}).get_text()

    # 0도 높아요
    weather_summary = soup.find("p",attrs={"class":"summary"}).find("span",attrs={"class":"weather before_slash"}).get_text()
    print(weather_summary,", 어제보다",weather_degree)

    summary = weather_summary + ", 어제보다" + weather_degree.strip()

    res = [temperature, summary]

    # 미세먼지, 초미세먼지, 자외선, 일몰
    chart_list = soup.find("ul",attrs={"class":"today_chart_list"}).find_all('li')
    chart_res = []
    for attrs in chart_list:
        print(attrs.get_text().strip())
        res.append(attrs.get_text().strip())
    print()
    
    return res


def scrape_news():
    url = 'https://news.naver.com'
    soup = create_soup(url)
    print('[헤드라인 뉴스]')
    hdline_article_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li",limit=3)
    res = []
    for index,li in enumerate(hdline_article_list):
        headline = li.find("a").get_text().strip()
        link = url + li.find("a")['href']
        print(f'{index+1}. {headline}')
        print(f'(링크 : {link})')
        res.append(f'{index+1}. {headline}')
        res.append(f'(링크 : {link})')
    print()

    return res

def scrape_IT_news():
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
    soup = create_soup(url)
    print('[IT 뉴스]')
    news_list = soup.find_all("div",attrs={"class":"cluster_group _cluster_content"},limit=3) # 3개까지만 가져오기
    res = []
    for index,li in enumerate(news_list):
        title = li.find("a",attrs={"class":"cluster_text_headline nclicks(cls_sci.clsart)"}).get_text()
        link = li.find("a",attrs={"class":"cluster_text_headline nclicks(cls_sci.clsart)"})['href']
        print(f'{index+1}. {title}')
        print(f'(링크 : {link}')
        res.append(f'{index+1}. {title}')
        res.append(f'(링크 : {link}')
    print()

    return res

def eng_today_conv():
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english'
    soup = create_soup(url)
    print('[오늘의 영어 회화]')
    today_sentence = soup.find("div",attrs={"class":"conv_titleTxt"}).get_text().strip()
    print(today_sentence)

    # 영어 지문 scraping
    conv_text = soup.find_all('div',attrs={"class":"conv_txt"})
    print('(영어 지문)')
    eng_sentences = []
    for sentence in conv_text[1].find_all("div"):
        print(sentence.get_text().strip())
        eng_sentences.append(sentence.get_text().strip())

    print()
    # 한글지문 scraping
    print('(한글 지문)')
    kor_sentences = []
    for sentence in conv_text[0].find_all("div"):
        print(sentence.get_text().strip())
        kor_sentences.append(sentence.get_text().strip())

    return today_sentence, eng_sentences, kor_sentences
    
if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_news() # 헤드라인 뉴스 가져오기
    scrape_IT_news() # IT 뉴스정보 가져오기
    eng_today_conv() # 해커스 오늘의 회화 가져오기