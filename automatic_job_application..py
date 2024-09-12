from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

user_name = "LINKEDIN-EMAIL"
password = "LINKEDIN-PASSWORD"

var = ("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&"
       "keywords=python%20developer&location=London%2C"
       "%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

url = 'https://www.linkedin.com/jobs/search'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(var)

sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

Enter_email = driver.find_element(By.ID, 'username')
Enter_password = driver.find_element(By.XPATH, '//*[@id="password"]')

Enter_email.send_keys(user_name)
Enter_password.send_keys(password)
time.sleep(2)
Enter_email.send_keys(Keys.RETURN)
job_search.send_keys('JOB-TITLE')
location.send_keys('YOUR-LOCATION')
job_search.send_keys(Keys.RETURN)


# TODO: This needs an authentication most of the time you can still complete it later.
