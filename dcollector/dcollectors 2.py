from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 1 open webdriver with selenium and catch page_souce
driver = webdriver.Chrome()
driver.get("url-to-collect")

# 2 create the ActionChains object by passing the driver object
action = ActionChains(driver);

# 3 Finding the first level menu object on the page using the 'find_element' method and moving the 
# cursor over this object using the 'move_to_element ()' method. Using the perform () method to 
# execute the actions we built on the action object. Doing the same for all objects.
menu = driver.find_element_by_xpath('//*[@id="main"]/header/nav/ul/li[1]/div[1]/a/img')

action.move_to_element(menu).perform()

linkxml = driver.find_element_by_xpath('//*[@id="main"]/header/nav/ul/li[1]/div[2]/ul[1]/li[5]/a')

action.move_to_element(linkxml).perform()

# 4 Clicking on the desired menu item using the click () method
linkxml.click()

# 5 Collecting page content using selenium's 'page_source'
xml = (driver.page_source)

# 6 Saving it to an .xml file
xmlarq = open('xml_source.xml', 'w')
xmlarq.write(xml)
xmlarq.close()