import time
from selenium.common import UnexpectedAlertPresentException, NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By

from main.alertHdlr import alertHdlr


def eduListClick(driver):
  driver.implicitly_wait(10)
  driver.get(
      'https://edu.gg.go.kr/front/mycampus/MyhomeAction.do?method=listStudy&TOPMENU_ID=1743&LEFTMENU_ID=1751&LEFTSUBMENU_ID=4231&mainCmd=1')

  driver.implicitly_wait(10)

  alertHdlr(driver)

  try:
    # '학습하기' 버튼을 찾기
    learn_button = driver.find_elements(By.CSS_SELECTOR, '.btn22_blue_03')[0]
    learn_button.click()

  except NoSuchElementException:
    print('No such element: .btn22_blue_03')
