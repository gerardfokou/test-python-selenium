#Assert the OrangeHRM login company branding is displayed
#Assert the HR for ALL logo is displayed
#Assert the Login text
#Assert that the Login data is diplaying Username: Admin and Password: admin123
#Assert the label Username and Password
#Assert Forgot your password? text
#Assert the OrangeHRM OS 5.5
#Assert the © 2005 - 2023 OrangeHRM, Inc. All rights reserved text
#Assert the OrangeHRM, Inc. link
#type username in the username field
#enter password in the password field
#click Login button
#click Forgot your password button
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

            
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
def assert_method(value, expected_text):
    element = driver.find_element(By.XPATH, value)
    actual = element.text
    print('Actual Text: ', actual) # Add this line to check the value of 'actual'
    assert actual == expected_text
#Assert the OrangeHRM login company branding is displayed
logo1_element = driver.find_element(By.XPATH, '//img[@alt="company-branding"]')
if logo1_element.is_displayed():
    print("OrangeHRM login company branding is displayed on the page")
else:
    print("OrangeHRM login company branding is displayed on the page")
#Assert the HR for ALL logo is displayed
logo2_element = driver.find_element(By.XPATH, '//img[@alt="orangehrm-logo"]')
if logo2_element.is_displayed():
    print("HR for ALL logo is displayed on the page")
else:
    print("HR for ALL logo is displayed on the page")
#Assert the Login text
try:
    assert_method('//h5[@class="oxd-text oxd-text--h5 orangehrm-login-title"]', 'Login')
    print('Login text assertion passed')
except AssertionError:
    print('Login text assertion failed')
#Assert that the Login data is diplaying Username: Admin and Password: admin123
try:
    assert_method('//p[@class="oxd-text oxd-text--p"]', 'Username : Admin')
    print('Usernamme assertion passed')
except AssertionError:
    print('Username assertion failed')
try:
    assert_method('//div/p[@class="oxd-text oxd-text--p"]', 'Password : admin123')
    print('Password assertion passed')
except AssertionError:
    print('Password assertion failed')
#Assert the label Username
try:
    assert_method('//label[@class="oxd-label"]', 'Username')
    print('Label username passed')
except AssertionError:
    print('Label username failed')
#Assert the label Password
try:
    assert_method('//div/label[@class="oxd-label"]', 'Password')
    print('Label password passed')
except AssertionError:
    print('Label password failed')
#Assert Forgot your password? text

time.sleep(3)
try:
  assert_method('//p[text()="Forgot your password? "]','Forgot your password')
  print('Forgot your password? text passed')
except AssertionError:
    print('Forgot your password? text failed')
#Assert the OrangeHRM OS 5.5
try:
    assert_method('//p[@class="oxd-text oxd-text--p orangehrm-copyright"]', 'OrangeHRM OS 5.5')
    print('OrangeHRM OS 5.5 passed')
except AssertionError:
    print('OrangeHRM OS 5.5 failed')
#Assert the © 2005 - 2023 OrangeHRM, Inc. All rights reserved text
try:
    assert_method('//p/a[@target="_blank"]', 'All right reserved')
    print('© 2005 - 2023 OrangeHRM, Inc. All rights reserved text passed')
except AssertionError:
    print('© 2005 - 2023 OrangeHRM, Inc. All rights reserved text failed')
#Assert the OrangeHRM, Inc. link
try:
    assert_method('//p/a[@target="_blank"]', 'OrangeHRM, inc')
    print('OrangeHRM, Inc. link passed')
except AssertionError:
    print('OrangeHRM, Inc. link failed')

#click Forgot your password button
time.sleep(3)
forgot_password_button= driver.find_element(By.XPATH, '//p[contains(@class, "orangehrm-login-forgot-header")]')
forgot_password_button.click()

time.sleep(3)
driver.back()
time.sleep(3)

#type username in the username field
username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
username_field.send_keys("Admin")
#enter password in the password field
password_field = driver.find_element(By.XPATH, '//input[@type = "password"]')
password_field.send_keys("admin123")
#click Login button
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()

time.sleep(20)
driver.quit()