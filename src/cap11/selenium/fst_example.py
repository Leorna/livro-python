from selenium import webdriver

try:
    browser = webdriver.Firefox()
    print(type(browser))
    browser.get('http://inventwithpython.com') #opens the firefox browser in the url passed in the argument
    elements_by_class_name = browser.find_elements_by_class_name('row')
    
    index = 0
    for element in elements_by_class_name:
        if index == 5:
            break
        print(f'{element.tag_name} {element.location} {element.text}')
        index += 1

except Exception as error:
    print(error)