import selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#prevent from the web page auto close



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
            jobs[n].click()
            time.sleep(5)
            applybuton = jobs[n].find_element(By.CLASS_NAME, "jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view")
            applybuton.click()
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR,"button.artdeco-button--tertiary").click()
            time.sleep(5)


        time.sleep(2)



linked = LinkedInJobs()
linked.login_linkedin()


class TokenGeneration:
    def token256(self):
        driver.get("https://generate-random.org/api-token-generator?count=1&length=256&type=mixed-numbers-symbols&prefix=")
        time.sleep(5)

        button = driver.find_element(By.CSS_SELECTOR, "button.btn-lg")
        button.click()
        time.sleep(5)
        token256 = driver.find_element(By.CSS_SELECTOR , "p.cursor-copy")
        print("Random Token 256Bit: " + token256.text)



# RandomToken = TokenGeneration()
# RandomToken.token256()
