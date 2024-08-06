from main.login import loginHdlr

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from main.runEdu import clickEduStart

chrome_options = Options()
service = Service( '/Users/jude/Local Storage/LocalCode/ChromeDriver/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

user_id = input('아이디를 입력하세요\n')
user_pwd = input('비밀번호를 입력하세요\n')

loginHdlr(user_id, user_pwd, driver)
clickEduStart(driver)

input("브라우저를 종료하려면 콘솔에서 Enter 키를 누르세요")
driver.quit()