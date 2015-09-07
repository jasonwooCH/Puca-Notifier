import urllib
import urllib2
import re
from cookielib import CookieJar

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

login_data = {
    "login":"homieplace@twc.com",
    "password":"pucabruin",
}

encoded_login = urllib.urlencode(login_data)

response = opener.open("https://pucatrade.com/login", encoded_login)

# test
# print re.findall("Dashboard" , response.read())

