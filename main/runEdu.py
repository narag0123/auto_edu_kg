import time
from selenium.common import UnexpectedAlertPresentException, \
  NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.by import By

from main.alertHdlr import alertHdlr
from main.eduListPage import eduListClick
from main.popUp_chapterList import popUp_chapterList


def clickEduStart(driver):

  # eduListClick(driver)

  driver.implicitly_wait(10)
  driver.get(
      'https://edu.gg.go.kr/front/mycampus/MyhomeAction.do?method=listStudy&TOPMENU_ID=1743&LEFTMENU_ID=1751&LEFTSUBMENU_ID=4231&mainCmd=1')

  driver.implicitly_wait(10)

  alertHdlr(driver)

  try:
    # '학습하기' 버튼을 찾기
    driver.implicitly_wait(10)
    learn_button = driver.find_elements(By.CSS_SELECTOR, '.btn22_blue_03')
    main_window = driver.current_window_handle

    for i in range(len(learn_button)):
      driver.implicitly_wait(10)
      driver.switch_to.window(main_window)
      learn_button[i].click()


      all_windows = driver.window_handles

      # 챕터들 나와있는 팝업 처리
      print(all_windows)
      driver.switch_to.window(all_windows[-1])
      popUp_chapterList(driver)

  except NoSuchElementException:
    print('No such element: .btn22_blue_03')

  driver.close()



