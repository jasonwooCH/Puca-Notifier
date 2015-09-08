from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import re

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

# access a page that requires you to be logged on
driver.get("https://pucatrade.com/trades")

# need to select the auto-match button to show only the cards we have
match_xpath = '//*[@id="content-wrapper"]/div[2]/div[3]/div[1]/label'
match_element = driver.find_element_by_xpath(match_xpath)
match_element.click()

# need to filter countries
country_xpath = '//*[@id="content-wrapper"]/div[2]/div[2]/div/div[1]/button'
country_element = driver.find_element_by_xpath(country_xpath)
country_element.click()

none_xpath = '//*[@id="flag-all"][2]'
none_element = driver.find_element_by_xpath(none_xpath)
none_element.click()
usa_xpath = '//*[@id="flag-71"]'
usa_element = driver.find_element_by_xpath(usa_xpath)
usa_element.click()
country_element.click()

# table_class = "card-table card-list-table dataTables_wrapper"
# card_table = driver.find_element_by_class_name(table_class)


# driver.quit()