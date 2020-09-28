from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


url = 'https://youtube.com'
browser = webdriver.Firefox()
browser.get(url)

page = browser.find_element_by_tag_name('html')
page.send_keys(Keys.END)
time.sleep(2)
page.send_keys(Keys.HOME)
time.sleep(5)
browser.quit()