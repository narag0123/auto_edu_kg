from selenium.common import NoAlertPresentException

def alertHdlr(driver):
  try:
    # 알림창이 나타나면, 포커스를 변경하고 확인을 클릭
    alert = driver.switch_to.alert
    alert.accept()  # 확인 버튼 클릭
    print("Alert accepted, continuing...")

  except NoAlertPresentException:
    print("No alert found.")

