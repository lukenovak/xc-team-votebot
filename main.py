from selenium import webdriver
from time import sleep

#do this through firefox
driver = webdriver.Firefox()

#get the page
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdscFnPYPSN5dhf6_HftZFcXW9kPZ68ANVZmE96uvIyoKBGQQ/viewform')

exception_count = 0

while True:
    try:
        vote_btn = driver.find_element_by_xpath('//div[@aria-label="Men\'s Cross Country - 1-2 Punch Earns Runner-up Finish"]')
        vote_btn.click()

        submit_button = driver.find_elements_by_class_name("freebirdFormviewerViewNavigationSubmitButton")
        submit_button[0].click()

        reload_button = driver.find_element_by_xpath("//*[text()='Submit another response']")
        reload_button.click()
        exception_count = 0
        sleep(0.5)
    except:
        exception_count += 1
        if exception_count < 3:
            print("there was some sort of exception! Sleeping for 30 seconds then retrying...")
            sleep(30)
        else:
            print("got tree consecutive exceptions- the server is likely moved or down. Exiting...")
            break
