from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from main.alertHdlr import alertHdlr
from main.popUpVideo import popUpVideo


def popUp_chapterList(driver):
  driver.implicitly_wait(10)

  chapterListWindow = driver.current_window_handle
  AllWindows = driver.window_handles

  # 교육의 갯수
  studyRunChkList = driver.find_elements(By.CSS_SELECTOR, '.goStudy')

  for videoIndex in range(len(studyRunChkList)):
    time_str_list = driver.find_elements(By.CSS_SELECTOR, '.cyberList > div.con > ul > li:nth-child(2)')[videoIndex]

    time_str =  time_str_list.text.split(': ')[1]
    end_mins = int(time_str.split('분')[0])
    end_secs = int(time_str.split('분')[1].split('초')[0])


    try:
      if(studyRunChkList[videoIndex].text != '복습하기'):
        el_study_name = driver.find_elements(By.CSS_SELECTOR, '.cyberList > div.con > ul > li.tit')
        print('-----------------------------------------------')
        print(f'{videoIndex + 1}차시 : {el_study_name[videoIndex].text}')

        studyRunChkList[videoIndex].click()
        driver.implicitly_wait(10)


        windows = driver.window_handles
        driver.switch_to.window(windows[-1])


        popUpVideo(driver, end_mins, end_secs)
        print('popUpVideo Activated !')
        driver.implicitly_wait(10)

        driver.switch_to.window(chapterListWindow)

        # 설문제출
        try:
          WebDriverWait(driver, 10).until(EC.alert_is_present())
          alertHdlr(driver)
        except TimeoutException:
          print("No Alert present")
    except NoSuchElementException:
      print("no ChkList")




  print('끝')
  driver.implicitly_wait(10)

