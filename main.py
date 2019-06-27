import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 10

url_main = "https://drive.google.com/drive/u/0/my-drive"
url_trash = "https://drive.google.com/drive/trash"
username = os.environ['GDRIVE_USER']
password = os.environ['GDRIVE_PSWD']

driver = webdriver.Chrome()

def login(url):

    driver.get(url)

    elem = driver.find_element_by_name("identifier")
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
    finally:
        elem = driver.find_element_by_name("password")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.title_is("My Drive - Google Drive")
        )
    finally:
        pass


def clear(url):

    driver.get(url)

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "a-l-S-Pc-w-d"))
        )
    finally:
        elem = driver.find_element_by_class_name("a-l-S-Pc-w-d")
        elem.click()
        elem.send_keys(Keys.DOWN)
        elem.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.NAME, "e"))
        )
    finally:
        driver.find_element_by_name("e").click()


def main():
    login(url_main)
    clear(url_trash)
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    main()
