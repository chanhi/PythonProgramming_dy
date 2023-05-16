# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
# selenium으로 키를 조작하기 위한 import
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
chrome_option.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_option)
'''
print("practice")
driver.get("https://www.naver.com")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(3)
title = driver.find_element(By.XPATH, "/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[10]/a/div[2]/div").text
print(title)
'''
'''
driver.get("https://land.naver.com/")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[1]/div/fieldset/input[6]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[1]/div/fieldset/input[6]").send_keys("압구정동 현대3차")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[1]/div/fieldset/a[1]/i").click()
time.sleep(1)
price = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/dl[1]/dd").text
rent_price = driver.find_element(By.XPATH, "/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/dl[2]/dd").text
print(price, rent_price)
'''

driver.get("https://finance.naver.com/")
time.sleep(1)
li = []
for i in range(1,11):
    company = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i}]/th/a").text
    percent = driver.find_element(By.XPATH, f'/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i}]/td[3]').text
    li.append([company, percent])

print(li)


