#Author:John Stonty

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import config


options = Options()
options.add_argument('--headless')
options.add_argument("--window-size=1440,900")
options.add_argument('--disable-gpu')
options.add_argument('--hide-scrollbars')
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"')

def init(targetID): 
    driver = webdriver.Chrome(chrome_options=options)
    wait = WebDriverWait(driver,300,0.01,None)
    driver.get('http:\\www.gmail.com')
    driver.find_element_by_id('identifierId').send_keys(config.username)
    driver.find_element_by_css_selector('[class="RveJvd snByac"]').click()
    #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(config.password)
    driver.find_element_by_css_selector('[class="RveJvd snByac"]').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loading"]/div[2]/div[4]')))
    driver.get('https://www.youtube.com/watch?v='+targetID)
    wait.until(EC.presence_of_element_located((By.ID, "chatframe")))
    driver.switch_to_frame("chatframe")
    return "inited"

def sendMessages(Message):
    driver = webdriver.Chrome(chrome_options=options)
    driver.find_element_by_xpath('//div[@id="input"]').send_keys(str(Message))
    driver.find_element_by_xpath('//yt-icon-button[@class="style-scope yt-button-renderer"]').click()
    # print("done.")

def stop():
    webdriver.Chrome(chrome_options=options).quit()