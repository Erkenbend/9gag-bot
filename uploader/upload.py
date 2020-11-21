from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException

import time
import os

opts = Options()

# Use next line to start browser in headless mode (invisible)
# opts.headless = True
# assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://9gag.com')

# Click "I accept" on cookie banner
nb_tries = 0
while nb_tries < 5:
    try:
        cookie_banner = WebDriverWait(browser, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, 'qc-cmp2-summary-buttons'))
        )
        # print(cookie_banner)
        time.sleep(1)
        buttons = cookie_banner.find_elements_by_xpath('.//*')
        for button in buttons:
            # print(button)
            if button.text == 'I ACCEPT':
                button.click()
                break

        break
    except StaleElementReferenceException as e:
        nb_tries += 1
        browser.refresh()

# Log in
login_button = browser.find_element_by_link_text('Log in')
login_button.click()

login_form = browser.find_element_by_id('login-email')

email_field = login_form.find_element_by_id('login-email-name')
email_field.send_keys('pupsmaschine5@gmail.com')  # TODO: get from file
pw_field = login_form.find_element_by_id('login-email-password')
pw_field.send_keys('Test1234+')  # TODO: get from file

login_form.submit()

# Upload file
time.sleep(2)
upload_button_candidates = browser.find_elements_by_class_name('btn-primary')  # .click()
for button in upload_button_candidates:
    # print(button)
    if button.text == 'Upload':
        button.click()
        break

file_upload_button_candidates = browser.find_elements_by_id('jsid-upload-file-btn')
for file_upload_button in file_upload_button_candidates:
    print(file_upload_button)
    # file_upload_button.click()
    path = os.getcwd() + '\\resources\\test.png'
    print(path)
    file_upload_button.send_keys(path)  # TODO: fix me

# Close browser
# browser.quit()
