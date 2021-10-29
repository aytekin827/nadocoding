from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

# user-agent 변수를 설정해주지 않으면 headlesschrome이라고 user-agent가 뜬다. 그렇게 되면 서버에서 접근을 막을 수도 있기때문에 headless를 사용할 때 이걸 설정해주는 것도 생각해놔야 한다.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.232 Whale/2.10.124.26 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.232 Whale/2.10.124.26 Safari/537.36

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()