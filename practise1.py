from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\pc\\Desktop\\selenium\\chromedriver.exe")

driver.get("https://www.testpine.com/")
print(driver.title)
driver.maximize_window()

goToApp= driver.find_element_by_css_selector("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a")
goToApp.click()

driver.refresh()

email=driver.find_element_by_id("email")
email.send_keys("sudesenacizmeci@gmail.com")
sifre=driver.find_element_by_id("password")
sifre.send_keys("sudeberkay1")
login=driver.find_element_by_css_selector("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button")
login.click()
time.sleep(3)

driver.save_screenshot("C:\\Users\\pc\\Desktop\\selenium\\ss.png")
time.sleep(0.5)

requirement=driver.find_element_by_css_selector("body > div > div > aside > div.nav-wrapper > ul > li:nth-child(2) > a")
requirement.click()
newRequirement=driver.find_element_by_id("returnList")
newRequirement.click()
requirementName=driver.find_element_by_name("requirementName")
requirementName.send_keys("practise")
requirementKayit=driver.find_element_by_id("btnAddRequirement")
requirementKayit.click()
time.sleep(5)



driver.quit()