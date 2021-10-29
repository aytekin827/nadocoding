from selenium import webdriver
browser = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser.maximize_window()

url = 'https://flight.naver.com/'
browser.get(url)

# 가는 날 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 27일, 28일 선택
browser.find_elements_by_css_selector("button.sc-crzoAE hnpClg inner")[0].click() # [0] -> 이번 달 

# browser.find_elements_by_class_name("sc-dIsUp jEEywD num")[0].click() # [0] -> 이번 달 
# 다음달 27일, 28일 선택
# browser.find_elements_by_class_name("27")[1].click() # [1] -> 다음 달 
# browser.find_elements_by_class_name("28")[1].click() # [1] -> 다음 달 
# # 이번달 27일 다음달 28일 선택
# browser.find_elements_by_class_name("27")[0].click() # [0] -> 이번 달 
# browser.find_elements_by_class_name("28")[1].click() # [1] -> 다음 달 

try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")))
    # 성공했을 때 수행 동작 위의 코드는 로딩을 기다려주도록 해주는 코드입니다
finally:browser.quit()