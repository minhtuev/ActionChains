from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
q_elem = driver.find_element_by_name("q")
q_elem.send_keys("selenium")
submit_elem = driver.find_element_by_name("submit")
action_chains = ActionChains(driver)
action_chains.move_to_element(submit_elem).click().perform()
assert driver.current_url == "https://www.python.org/search/?q=selenium&submit="
driver.close()