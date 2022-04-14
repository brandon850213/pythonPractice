from email import message
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()
user_message.send_keys('I AM COOOOOL')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'I AM COOOOOL' in output_message.text

# chrome_browser.close()
# chrome_browser.close() #close twice due to sometimes bug
chrome_browser.quit()
