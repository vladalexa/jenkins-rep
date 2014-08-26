import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'os': 'Windows', '8': 'xp', 'browser': 'chrome', 'browser_version': '36'}

# driver = webdriver.Remote(
#     command_executor='http://127.0.0.1:4444/wd/hub',
#     desired_capabilities=desired_cap)
driver=webdriver.Firefox()

driver.get("http://google.co.uk")
driver.maximize_window()
# email = driver.find_element_by_name("email")
# email.send_keys("vlad@affectv.co.uk")
# password=driver.find_element_by_name("password")
# password.send_keys("affectv123")
# password.submit()
# driver.find_element_by_xpath("/html/body/nav/div[8]/a/span[1]").click()

# try:
#     assert "Advertiser list" == driver.title
# except ValueError:
#     print "WRONG TITLE"
sys.stdout.flush()
print '*******************'
print driver.title
print'******************'
driver.quit()