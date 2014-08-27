import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# desired_cap = {'browser': 'firefox',}

# driver = webdriver.Remote(
#      command_executor='http://127.0.0.1:4444/wd/hub',
#      desired_capabilities=DesiredCapabilities.FIREFOX)
driver=webdriver.Firefox()

driver.get("http://google.co.uk")
driver.maximize_window()
# email = driver.find_element_by_name("email")
# email.send_keys("vlad@affectv.co.uk")
# password=driver.find_element_by_name("password")
time.sleep(3)
print '*****************'
print driver.title
print'******************'
driver.quit()
