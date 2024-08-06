import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



from main.alertHdlr import alertHdlr


def popUpVideo(driver, end_mins, end_secs):
  driver.implicitly_wait(10)

  try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alertHdlr(driver)
  except TimeoutException:
    print("No Alert present")

  driver.implicitly_wait(10)


  # 비디오에 마우스 호버
  try:
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, 'main'))
    )
    hoverEl = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#video_display'))
    )
    actions = ActionChains(driver)
    actions.move_to_element(hoverEl).perform()

    # hover 후 기다리면 동작
    totalTime = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#video_controlbar_duration'))
    )


    minutes, seconds = totalTime.text.split(':')
    mins = int(minutes)
    secs = int(seconds)
    print(f'전체 영상 길이 : {mins}분 {secs}초')

    standardTimeSec = end_mins * 60 + end_secs
    print(f'재생 길이 : {end_mins}분 {end_secs}초')
    time.sleep(standardTimeSec + 50) # 교육수료까까지 필요한 시간 대기


  except TimeoutException:
    print("No video")
  finally:
    driver.switch_to.default_content()  # 프레임에서 벗어나기
    driver.close()
