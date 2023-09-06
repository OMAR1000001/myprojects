from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

email="**************************"
pswd="**************"


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%2522xa0h3lf0s651gq01s539v6ug15ceyamw45ek31347tosdcy0yl%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Den_US%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D29953ff9-7e2b-4765-9018-0424778cff60%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522xa0h3lf0s651gq01s539v6ug15ceyamw45ek31347tosdcy0yl%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=page&locale=en_GB&pl_dbl=0")
time.sleep(5)
lgin=driver.find_element(By.XPATH,'//*[@id="email"]')
lgin.send_keys(email)
pswrrd=driver.find_element(By.XPATH,'//*[@id="pass"]')
pswrrd.send_keys(pswd)
pswrrd.send_keys(Keys.ENTER)
time.sleep(10)
sgin=driver.find_element(By.CSS_SELECTOR,'._ab21 button')
sgin.send_keys(Keys.ENTER)
time.sleep(10)

driver.get('https://www.instagram.com/messi.the.alien/')
time.sleep(5)

dos=driver.find_element(By.XPATH,'//*[@id="mount_0_0_aJ"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]')
dos.click()
input("")
# driver.get('https://www.instagram.com/messi.the.alien/followers/')
# time.sleep(5)
# follow=driver.find_elements(By.CSS_SELECTOR,'._aano button')
#
# for followr in follow:
#     followr.click()
#     time.sleep(2)



