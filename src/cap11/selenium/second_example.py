from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    element = browser.find_element_by_class_name('bookcover')
    print(f'Found {element.tag_name} element with that class name!')
except:
    print('Was not able to find an element with a bookcover class')
