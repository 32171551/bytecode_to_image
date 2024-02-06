from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


URL = "https://etherscan.io/contractsVerified"

ex_path = 'C:\\chromedriver_win32\\chromedriver.exe'
chrome_options = Options()
driver = webdriver.Chrome(executable_path=ex_path, options=chrome_options)
driver.get(url=URL)
driver.implicitly_wait(10)

data = []

show_row = driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/form/div[3]/div/select").send_keys(Keys.ENTER)
row_100 = driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/form/div[3]/div/select/option[4]").click()
for a in range(5):
    a = a+1
    for i in range(100):
        i = i+1
        address = driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/div[3]/table/tbody/tr[{}]/td[1]/span/a[1]".format(i)).get_attribute('href')
        data.append(address)
        # print(data)
        driver.implicitly_wait(10)
        if i == 100:
            i = 0
            print("page end")
            driver.implicitly_wait(30)
    if a == 5:
        break
    next_page = driver.find_element(By.XPATH,"/html/body/main/section[2]/div[1]/form/div[3]/nav/ul/li[4]/a").send_keys(Keys.ENTER)
    driver.implicitly_wait(30)

print(data)

filePath = './addr_list.txt'
with open(filePath, 'w+') as lf:
    lf.write('\n'.join(data))