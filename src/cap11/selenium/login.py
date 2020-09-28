from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://www.stoodi.com.br/login')

try:
    user_name = ''
    password = ''

    login_name = browser.find_element_by_id('loginName')
    login_password = browser.find_element_by_id('loginPassword')
    
    print(type(login_name))
    print(type(login_password))

    login_name.send_keys(user_name)
    login_password.send_keys(password)
    
    login_password.submit()
except Exception as error:
    print(error)