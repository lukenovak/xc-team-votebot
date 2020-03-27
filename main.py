from selenium import webdriver
from time import sleep

#do this through firefox
driver = webdriver.Firefox()
score_tracker = webdriver.Firefox()

#get the page
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdscFnPYPSN5dhf6_HftZFcXW9kPZ68ANVZmE96uvIyoKBGQQ/viewform')
score_tracker.get('https://docs.google.com/forms/d/e/1FAIpQLSdscFnPYPSN5dhf6_HftZFcXW9kPZ68ANVZmE96uvIyoKBGQQ/viewanalytics')

#get the current percentage

current_score_text = score_tracker.find_element_by_css_selector('#c0 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1) > g:nth-child(4) > text:nth-child(2)').text
current_score = float(current_score_text.strip('%'))
vote_number = 1

exception_count = 0

while True:
    #only vote if we are less than 2% ahead
    if current_score < 52:
        try:
            vote_btn = driver.find_element_by_xpath('//div[@aria-label="Men\'s Cross Country - 1-2 Punch Earns Runner-up Finish"]')
            vote_btn.click()

            submit_button = driver.find_elements_by_class_name("freebirdFormviewerViewNavigationSubmitButton")
            submit_button[0].click()

            reload_button = driver.find_element_by_xpath("//*[text()='Submit another response']")
            reload_button.click()
            exception_count = 0
            sleep(0.5)
            vote_number = vote_number+1
            #check the score after voting 50 times
            if vote_number > 50:
                score_tracker.refresh()
                current_score_text = score_tracker.find_element_by_css_selector('#c0 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1) > g:nth-child(4) > text:nth-child(2)').text
                current_score = float(current_score_text.strip('%'))
                vote_number = 0
        except:
            exception_count += 1
            if exception_count < 3:
                print("there was some sort of exception! Sleeping for 30 seconds then retrying...")
                sleep(30)
            else:
                print("got tree consecutive exceptions- the server is likely moved or down. Exiting...")
                break
       
    #sleep for 2 minutes if we are ahead by too much before checking again
    else:
        sleep(120)
        current_score_text = score_tracker.find_element_by_css_selector('#c0 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(1) > g:nth-child(4) > text:nth-child(2)').text
        current_score = float(current_score_text.strip('%'))
