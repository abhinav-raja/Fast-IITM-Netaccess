#----Enter LDAP username and password here---
username = ""
password = ""
#--------------------------------------------


from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
service = Service(executable_path="chromedriver.exe")

#Open netAccess
driver = webdriver.Chrome(service=service)
driver.get("https://netaccess.iitm.ac.in")

#Enter Username and Password
usernameInp = driver.find_element(By.ID, "username")
usernameInp.clear()
usernameInp.send_keys(username)
pwInp = driver.find_element(By.ID, "password")
pwInp.clear()
pwInp.send_keys(password)
#Entering RETURN after filling in password submits the form
pwInp.send_keys(Keys.RETURN)

#Wait a bit to ensure login is successful
time.sleep(2.5)

#Navigate to the approval page
driver.get("https://netaccess.iitm.ac.in/account/approve")
#Select the option for 1 day and approve
oneDayEl = driver.find_element(By.ID, "radios-1")
oneDayEl.click()
authorizeEl = driver.find_element(By.ID, "approveBtn")
authorizeEl.click()

#End
driver.quit()

