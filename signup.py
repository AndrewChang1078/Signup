import os
from selenium import webdriver
driver = webdriver.Chrome()

# Modify these variable before use
my_seat_num='$SeatNumber'
my_email='$Email'
my_pwd='$Password'

# Login
driver.get('https://www.signupgenius.com/register')
email=driver.find_element('xpath', '//*[@id="email"]')
email.send_keys(my_email)
password=driver.find_element('xpath', '//*[@id="pword"]')
password.send_keys(my_pwd)
login_btn=driver.find_element('xpath', '//*[@id="loginBtnId"]')
login_btn.click()

# Signup
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.signupgenius.com/go/10C084DABAD2BA7F9C34-cubicle1#/')
driver.implicitly_wait(5000)
my_seat_btns=driver.find_elements('xpath', "//*[text()='"+my_seat_num+"']/../../../../preceding-sibling::div[1]/signup-button/button")
for my_seat_btn in my_seat_btns:
    if 'Sign Up' in my_seat_btn.text:
        driver.execute_script("arguments[0].click();", my_seat_btn)
privacy_confirm_btn=driver.find_element('xpath', '/html/body/div[3]/div/span[2]/a')
privacy_confirm_btn.click()
save_btn=driver.find_element('xpath', '//*[@id="signupContainerId"]/div[4]/div/button')
save_btn.click()
signup_btn=driver.find_element('xpath', '//*[@id="SUGContainer"]/div[3]/div/div/div/div[3]/div/span/span[2]/button')
driver.execute_script("arguments[0].click();", signup_btn)
os.system("pause")
