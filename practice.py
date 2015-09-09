import requests
import re

login_data = {
    "login":"homieplace@twc.com",
    "password":"pucabruin",
}

session = requests.Session()

session.post("https://pucatrade.com/login", data = login_data)

# test
# r = session.get("https://pucatrade.com/dashboard")
# print r.text

r = session.get("https://pucatrade.com/trades")
# need to scrape here.

print re.findall("niceToggle intersect on", r.text)
# Setting needs to be switched to Auto-matching so that this is found
