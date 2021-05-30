from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import pyautogui, pyperclip, random, time

chrome_options = webdriver.ChromeOptions()
prefs = {
	"profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_extension('./SelectorsHub.crx')
driver = webdriver.Chrome('./chromedriver', chrome_options = chrome_options)

driver.get("https://www.facebook.com/")

input_search = driver.find_element_by_css_selector('#email')
input_search.send_keys('0935362612')
js2 = "document.querySelectorAll('input')[3].value='120299Thinh5'"
driver.execute_script(js2)
pyautogui.press("enter")
driver.get("https://www.facebook.com/photo?fbid=3515558795236925&set=a.241819132610924")
# driver.find_element_by_css_selector('a[aria-label=\"Tin của Nguyễn Trang\"] div[class=\"mm8kr34x i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4\"]').click()
# timkiem = driver.find_element_by_css_selector('input[ placeholder =\'Tìm kiếm trên Facebook\']')
# timkiem.send_keys('tienthinh12102')
time.sleep(3)
driver.find_element_by_css_selector('div[class=\'tvfksri0 ozuftl9m jmbispl3 olo4ujb6\'] div[aria-label=\'Thích\'] div[class=\'rq0escxv l9j0dhe7 du4w35lb j83agx80 g5gj957u rj1gh0hx buofh1pr hpfvmrgz taijpn5t bp9cbjyn owycx6da btwxx1t3 d1544ag0 tw6a2znq jb3vyjys dlv3wnog rl04r1d5 mysgfdmx hddg9phg qu8okrzs g0qnabr5\']').click()

