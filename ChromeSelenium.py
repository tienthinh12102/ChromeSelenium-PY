from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

chrome_options = webdriver.ChromeOptions()
prefs = {
	# "profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('./chromedriver', chrome_options = chrome_options)

driver.get("https://www.google.com/")

#Cách 1 dùng js click
# js = "document.querySelector('.read-more').click()"
# driver.execute_script(js)
#Cách 2 dùng driver tim phan tử
# driver.find_element_by_css_selector('.read-more').click()

#Điền chữ
#Cách 1 js
js= "document.querySelector('input[name=\"q\"]').value='thinh-sama'"
driver.execute_script(js)
js2= "document.querySelectorAll('center input')[2].click()"
driver.execute_script(js2)
js3 = "document.querySelectorAll('div')[32].click()"
driver.execute_script(js3)

#Cách 2 driver
input_search = driver.find_element_by_css_selector('input[name="q"]')
input_search.send_keys('thinh-sama123')
js4 = "document.querySelectorAll('button')[0].click()"
driver.execute_script(js4)