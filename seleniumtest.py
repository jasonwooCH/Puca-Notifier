from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://pucatrade.com")

puca_username  = "homieplace@twc.com"
puca_password = "pucabruin"

user_fieldID = "login"
pass_fieldID = "password"
login_btnxpath = '//*[@id="home-login"]/form/div[4]/button'

# there is one more id="login", make sure its in the div with id="home-login"
form = driver.find_element_by_id("home-login")

user_fieldelement = form.find_element_by_id(user_fieldID)
pass_fieldelement = form.find_element_by_id(pass_fieldID)
login_btnelement  = form.find_element_by_xpath(login_btnxpath)

# if there are any texts in the element, clear, then simulate typing into element with send_keys()
user_fieldelement.clear()
user_fieldelement.send_keys(puca_username)
pass_fieldelement.clear()
pass_fieldelement.send_keys(puca_password)
login_btnelement.click()  # clicks the element
