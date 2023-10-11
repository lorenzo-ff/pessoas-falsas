# LOGIN
user = ''
psswrd = ''

# IMPORTS
from selenium import webdriver
from selenium.webdriver import chrome
from time import sleep
from getpass import getpass
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# OPEN CHROME
option = webdriver.ChromeOptions()
#set chrome to English, so we can find element easiler 
option.add_argument('--lang=en-US')
#change size of chrome (option)
option.add_argument('--window-size=1200,1000')
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))

# OPEN INSTAGRAM
driver.get("http://www.instagram.com")
sleep(1)
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username_input.send_keys(f"{user}")
password_input.send_keys(f"{psswrd}")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']"); login_button.click()
sleep(3)

# FOLLOWING LIST
# open followings
driver.get(f"https://www.instagram.com/{user}/following/")
sleep(3)
# scrolling down (open all followings)
while True:
    try:
        element = driver.find_element(By.XPATH, '//*[@class="_aanq"]')
        driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(2.5)
    except:
        break
# following list
im_fllwng = []
for e in driver.find_elements(By.XPATH, '//*[@class="_aacl _aaco _aacw _aacx _aad7 _aade"]'):
    im_fllwng.append(e.text)
print(len(im_fllwng))
sleep(10)

# FOLLOWERS LIST
# open followers
driver.get(f"https://www.instagram.com/{user}/followers/")
sleep(3)
# scrolling down (open all followers)
while True:
    try:
        element = driver.find_element(By.XPATH, '//*[@class="_aanq"]')
        driver.execute_script("arguments[0].scrollIntoView();", element)
        sleep(2.5)
    except:
        break
# followers list
my_fllwrs = []
for e in driver.find_elements(By.XPATH, '//*[@class="_aacl _aaco _aacw _aacx _aad7 _aade"]'):
    my_fllwrs.append(e.text)
print(len(my_fllwrs))
sleep(10)

# GENTE FALSA (FAKE PEOPLE)
gente_falsa = list(set(im_fllwng).difference(set(my_fllwrs)))
print(gente_falsa)

# END
sleep(60)
driver.close()