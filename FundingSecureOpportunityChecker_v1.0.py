import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

username = "enter_username_here"
password = "enter_password_here"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.fundingsecure.com/signin")
driver.find_element_by_id("memUsername").send_keys(username)
driver.find_element_by_id ("memPassword").send_keys(password)
driver.find_element_by_class_name("btn-block").click()
el = driver.page_source
soup = BeautifulSoup(el)

loanBoxes = soup.find_all("div", {"class" : "loanBox"})

def fetchTitles():
    titles = (soup.find_all("div", {"class" : "loanBoxTitle"}))
    for x in range(0, len(titles)): titles[x] = titles[x].h3.text
    return titles
def fetchRates():
    return [x.find_all("div", {"class" : "row"})[2].find_all("div")[1].text for x in loanBoxes]
def fetchTerms():
    return [x.find_all("div", {"class" : "row"})[3].find_all("div")[0].text for x in loanBoxes]
def fetchLTVs():
    return [x.find_all("div", {"class" : "row"})[3].find_all("div")[1].text for x in loanBoxes]


titles = fetchTitles()
rates = fetchRates()
terms = fetchTerms()
LTVs = fetchLTVs()

def fetchTuples():
    return [{
     "Title" : titles[i].split("-")[1][1:],
     "Rate" : rates[i].split(" ")[1],
     "Months" : terms[i].split(" ")[1],
     "LTV" : LTVs[i].split(" ")[1]
     } for i in range(0, len(titles))]

tuples = fetchTuples()

for x in titles: print(x)
for x in rates: print(x)
for x in terms: print(x)
for x in LTVs: print(x)
for x in tuples: print(x)
