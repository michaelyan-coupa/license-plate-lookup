from selenium import webdriver

webpage = r"https://findbyplate.com/" # edit me
searchterm = "2LB117" # edit me

driver = webdriver.Chrome()
driver.get(webpage)

sbox = driver.find_element_by_class_name("platenumber")
sbox.send_keys(searchterm)

select = Select(driver.find_element_by_id('location'))
# select by visible text
select.select_by_visible_text('West Virginia')


submit = driver.find_element_by_class_name("sbtSearch")
submit.click()
