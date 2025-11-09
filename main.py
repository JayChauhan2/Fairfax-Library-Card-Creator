import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()

# Open a page
driver.get("https://fcplcat.fairfaxcounty.gov/patronaccount/selfregister.aspx?ctx=1.1033.0.0.1")
# print(driver.page_source) #vomit the html

home_library = driver.find_element(By.NAME, "ctl00$BodyMainContent$lstBranches")
zip_code = driver.find_element(By.NAME, "ctl00$BodyMainContent$txtZipCode")

# Wrap it in a Select object
select = Select(home_library)

# Select by visible text (what the user sees in the dropdown)
select.select_by_visible_text("City of Fairfax Regional Library")
zip_code.send_keys("12345") #zipcode

submit_button = driver.find_element(By.NAME, "ctl00$BodyMainContent$btnSubmitBranchAndZip")
submit_button.click()

wait = WebDriverWait(driver, 2)  # wait up to 2 seconds
new_element = wait.until(
    EC.presence_of_element_located((By.NAME, "txtNameFirst")) #first name text input
)
print("New page loaded!")

text = f"jay{random.randint(1, 10000)}"
driver.find_element(By.NAME, "txtNameFirst").send_keys(text)
driver.find_element(By.NAME, "txtNameLast").send_keys(text)

driver.find_element(By.NAME, "txtBirthdatemm").send_keys("01")
driver.find_element(By.NAME, "txtBirthdatedd").send_keys("01")
driver.find_element(By.NAME, "txtBirthdateyyyy").send_keys("2000")

driver.find_element(By.NAME, "txtStreet1").send_keys("Your Address")

driver.find_element(By.NAME, "txtEmail").send_keys("email@gmail.com")


home_library = Select(driver.find_element(By.NAME, "txtUDF3")).select_by_visible_text("NO")

driver.find_element(By.NAME, "txtUsername").send_keys(text)
driver.find_element(By.NAME, "txtPassword").send_keys(text)
driver.find_element(By.NAME, "txtVerification").send_keys(text)

driver.find_element(By.NAME, "btnSubmitMainForm").click()

wait = WebDriverWait(driver, 2)  # wait up to 2 seconds
new_element = wait.until(
    EC.presence_of_element_located((By.ID, "content")) #main content thing
)
print("New page loaded!")

b_element = driver.find_element(
    By.XPATH,
    "(//form[@id='formMain']//div[contains(@class, 'content-container')][1]//b)[1]"
)

print("user: ", str(b_element.text))
print("password: ", text)

driver.quit()
