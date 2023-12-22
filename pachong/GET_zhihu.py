from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

username = 'lqx1213'
password = 'lqx19961213'
# options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome()
#显示等待需要用到
wait = WebDriverWait(driver,10)
driver.get('https://www.duitang.com/category/?cat=wallpaper')
driver.maximize_window()
try:
    name_ele = wait.until(EC.visibility_of_element_located((By.ID,"p-username")))
    name_ele.send_keys(username)
    ps_ele = wait.until(EC.visibility_of_element_located((By.ID,"p-password")))
    ps_ele.send_keys(password)
    time.sleep(2)
    check_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"pg-loginbtn")))
    check_button.click()
except Exception as e:
    print("未找到元素，原因如下：{}".format(e))
# alert = driver.switch_to.alert
# alert_text = alert.text
# alert.accept()
slip_time = 2
scroll_high = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(slip_time)

    # 计算滚动高度的变化，判断是否已经到达底部
    new_scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if new_scroll_height == scroll_high:
        break
    scroll_height = new_scroll_height

# ele = driver.find_element(By.CSS_SELECTOR,'body > div.blockUI.blockMsg.blockPage > div > div.tt-s > a').click()
print(driver.page_source)