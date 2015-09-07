import requests

login_data = {
    "login":"homieplace@twc.com",
    "password":"pucabruin",
}

session = requests.Session()

session.post("https://pucatrade.com/login", data = login_data)

#test
r = session.get("https://pucatrade.com/dashboard")

print r.text
