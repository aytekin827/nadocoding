from selenium import webdriver
import time
browser = webdriver.Chrome() # 경로정보를 변수로 넣어주어야 함

# 네이버 이동
browser.get("http://naver.com")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# id.pw입력
browser.find_element_by_id("id").send_keys("scv186921")
browser.find_element_by_id("pw").send_keys("")

# 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()
time.sleep(3)
# id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("new_id")

# html정보 출력
print(browser.page_source)

# 브라우저 종룔
browser.close() # 현재 탭만 종료
# browser.quit() # 전체 브라우저 종료