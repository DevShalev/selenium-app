import selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#prevent from the web page auto close
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

TCB_USERNAME = ""
TCB_PASSWORD = ""

linkedin_pass = ""


service = Service(r"C:\Users\shale\Desktop\DevOps\DevOpsCourse4months\softwares\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

class LoginToTcb:
    def login_step_1(self):
        driver.get("https://login.tcb.ac.il/nidp/saml2/sso?id=tcbloa2&sid=1&option=credential&sid=1")
        time.sleep(5)

        username = driver.find_element(By.ID, "Ecom_User_ID")
        username.send_keys(TCB_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(5)

    def login_step_2(self):
        time.sleep(5)
        link = driver.find_element(By.ID, "ldapPasswordCard")
        link.click()
        time.sleep(5)

    def login_step_3(self):
        time.sleep(5)
        password = driver.find_element(By.ID, "ldapPassword")
        password.send_keys(TCB_PASSWORD)
        password.send_keys(Keys.ENTER)
        #prevent from the web page to auto close!
        chrome_options.add_experimental_option("detach", True)
        time.sleep(10)


# tcb = LoginToTcb()
# tcb.login_step_1()
# tcb.login_step_2()
# tcb.login_step_3()

#https://www.linkedin.com/jobs/search/?currentJobId=3676652492&f_AL=true&f_WT=3%2C1&keywords=full%20stack%20developer&refresh=true&sortBy=R


class LinkedInJobs:
    def login_linkedin(self):
        driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
        time.sleep(5)
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("")
        password.send_keys(linkedin_pass)
        password.send_keys(Keys.ENTER)

        time.sleep(10)

        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3676652492&f_AL=true&f_WT=3%2C1&keywords=full%20stack%20developer&refresh=true&sortBy=R")

        time.sleep(10)

        jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-list a")
        for n in range(len(jobs)):
            print(jobs[n].text)

        chrome_options.add_experimental_option("detach", True)


linked = LinkedInJobs()
linked.login_linkedin()