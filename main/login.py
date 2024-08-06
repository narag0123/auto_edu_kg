from selenium.common import NoSuchElementException, NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time


def loginHdlr(idValue, pwdValue, driver):
  loginURL = 'https://edu.gg.go.kr/front/member/LoginAction.do?method=login'

  driver.get(loginURL)
  time.sleep(2)

  idInput = driver.find_element(By.NAME, 'loginId')
  pwdInput = driver.find_element(By.NAME, 'loginPwd')

  idInput.send_keys(idValue)
  pwdInput.send_keys(pwdValue)
  pwdInput.send_keys(Keys.RETURN)

  driver.implicitly_wait(10)

  try:
    elgreyBox = driver.find_element(By.CSS_SELECTOR, '.btn22_grey_02.btn-cancel')
    elgreyBox.click()
  except NoSuchElementException:
    print('no grey box')
