from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    links = browser.find_elements_by_tag_name('a')
    for link in links:
        if link.text == 'YouTube':
            link.click()
            break
except Exception as error:
    print(error)